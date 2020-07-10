var name = 'zero';

function wrapper() {
  var name = 'nero';
  log();
}
function log() {
  console.log(name);
}
wrapper();