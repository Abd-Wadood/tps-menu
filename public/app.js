// Both branch contacts and the original PDF work without JavaScript.
// Preserve existing QR links that identify a branch.
const branch = new URLSearchParams(location.search).get('branch');
if (branch === 'barki-road' || branch === 'bedian-road') {
  document.getElementById(branch)?.setAttribute('data-selected', 'true');
}
