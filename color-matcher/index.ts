import ImageColorService from './image-color-service';
import * as path from 'path';

const imageColorService = ImageColorService.getInstance();

const imagePath1 = path.join(__dirname, 'path/to/image1.jpg');
const imagePath2 = path.join(__dirname, 'path/to/image2.jpg');

const criteria = {
  hueDiffThreshold: 150,
  saturationDiffThreshold: 30,
  lightnessDiffThreshold: 30,
  excludeBackground: true
};

async function analyzeImages() {
  try {
    const colors1 = await imageColorService.processFile(imagePath1, criteria);
    const colors2 = await imageColorService.processFile(imagePath2, criteria);

    const match = imageColorService.analyzeColors(colors1, colors2, criteria);
    console.log(`Do the images match? ${match}`);
  } catch (error) {
    console.error('Error analyzing images:', error);
  }
}

analyzeImages();
