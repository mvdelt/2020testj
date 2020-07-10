const mkdirj = require('../nodeCodesj/makeDirTestj')


mkdirj(__dirname + '/importAndMakeDirTestj', 0744, function(err) {
    if (err){
        // handle folder creation error
        console.error(err)
    } 
    else{ // we're all good
        console.log('j) mkdir successfully finished.')
    }
})