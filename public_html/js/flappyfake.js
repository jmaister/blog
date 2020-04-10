var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

var baseImage = new Image();
baseImage.onload = function() {
    context.drawImage(baseImage, 0, 0);
};
baseImage.src = 'http://i.imgur.com/oNRqg7v.png';

// Load images
var imageSrc = [];
imageSrc[0] = 'http://i.imgur.com/3Fk36Ax.png';
imageSrc[1] = 'http://i.imgur.com/qHt2rZ9.png';
imageSrc[2] = 'http://i.imgur.com/3lme2TS.png';
imageSrc[3] = 'http://i.imgur.com/oC82akz.png';
imageSrc[4] = 'http://i.imgur.com/AcWogHV.png';
imageSrc[5] = 'http://i.imgur.com/mZYEQm2.png';
imageSrc[6] = 'http://i.imgur.com/PjGLhAO.png';
imageSrc[7] = 'http://i.imgur.com/bTy7HbP.png';
imageSrc[8] = 'http://i.imgur.com/0EdVGm4.png';
imageSrc[9] = 'http://i.imgur.com/K1MgIb5.png';


var images = [];
for ( i = 0; i < 10; i++) {
    images[i] = new Image();
    images[i].src = imageSrc[i];
}



function draw() {
    var score = document.getElementById('score').value;
    context.drawImage(baseImage, 0, 0);

    var y1 = 525;
    var y2 = 630;
    var x = 586;
    for ( i = score.length - 1; i >= 0; i--) {
        var digit = parseInt(score[i]);
        var img = images[digit];
        context.drawImage(img, x - img.width, y1);
        context.drawImage(img, x - img.width, y2);
        x = x - img.width - 6;
    }
};
