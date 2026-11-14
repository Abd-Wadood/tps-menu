import assert from 'node:assert/strict';
import {readFile,access} from 'node:fs/promises';
const html=await readFile('public/index.html','utf8');
for(const href of ['tel:+923239091177','tel:+923082566477','https://wa.me/923018408177','https://wa.me/923082566477'])assert(html.includes(href));
assert(html.includes('download="The-Pizza-Shop-Menu.pdf"'));
await access('public/menus/original-menu.pdf');await access('public/assets/logo.webp');
console.log('PASS: original PDF, logo, download and both branch contact links.');

