var name = 'zero';

function wrapper() {
    name = 'nero';
    log();
}
function log() {
  console.log(name);
}
wrapper();