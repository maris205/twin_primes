#!/usr/bin/env node
// Isolated server-side MathJax 3.2.2 compatibility probe, not an Obsidian UI test.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const vault = path.resolve(__dirname, '..');
const moduleRoot = process.argv[2];
if (!moduleRoot) throw new Error('Usage: node check_mathjax.cjs /path/to/node_modules');
const library = path.join(path.resolve(moduleRoot), 'mathjax-full');
const {mathjax} = require(path.join(library, 'js/mathjax.js'));
const {TeX} = require(path.join(library, 'js/input/tex.js'));
const {SVG} = require(path.join(library, 'js/output/svg.js'));
const {liteAdaptor} = require(path.join(library, 'js/adaptors/liteAdaptor.js'));
const {RegisterHTMLHandler} = require(path.join(library, 'js/handlers/html.js'));
const {AllPackages} = require(path.join(library, 'js/input/tex/AllPackages.js'));
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const packages = AllPackages.filter(p => !['noundefined', 'noerrors', 'autoload', 'require'].includes(p));
const tex = new TeX({packages, maxMacros:10000, maxBuffer:200000,
                    formatError(jax,error) {throw error;}});
const document = mathjax.document('', {InputJax:tex, OutputJax:new SVG({fontCache:'none'})});
const nodes = JSON.parse(fs.readFileSync(path.join(vault,'.build/math_nodes.json'),'utf8'));
const unique = new Map();
const failures = [];
let checked = 0;
for (const node of nodes) {
  const key = node.kind+'\0'+node.tex;
  if (!unique.has(key)) {
    let problem = null;
    try {
      tex.reset();
      const output = document.convert(node.tex, {display:node.kind === 'DisplayMath'});
      const svg = adaptor.outerHTML(output);
      if (svg.includes('data-mjx-error') || svg.includes('data-mml-node="merror"')) {
        problem = 'MathJax emitted an error node';
      }
    } catch(error) { problem = String(error.message || error); }
    unique.set(key,problem);
    checked++;
    if (checked%4000 === 0) process.stdout.write('MathJax unique expressions checked: '+checked+'\n');
  }
  if (unique.get(key)) failures.push({...node,error:unique.get(key)});
}
const data = {
  scope:'Server-side MathJax compatibility, not desktop Obsidian or mathematical verification',
  version:require(path.join(library,'package.json')).version,
  totalExpressions:nodes.length,uniqueExpressions:unique.size,
  failedOccurrences:failures.length,
  failedUnique:[...unique.values()].filter(Boolean).length,
  input_sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(vault,'.build/math_nodes.json'))).digest('hex'),
  failures
};
fs.writeFileSync(path.join(vault,'.build/mathjax_report.json'),JSON.stringify(data,null,2)+'\n');
process.stdout.write(JSON.stringify({...data,failures:failures.slice(0,12)},null,2)+'\n');
