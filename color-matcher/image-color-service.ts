import * as fs from 'fs';
import getColors from 'get-image-colors';
import getPixels from 'get-pixels';
import * as colorConvert from 'color-convert';

interface MatchingCriteria {
  hueDiffThreshold?: number;
  saturationDiffThreshold?: number;
  lightnessDiffThreshold?: number;
  excludeBackground?: boolean;
}

class ImageColorService {
  private static instance: ImageColorService;

  private constructor() {}

  static getInstance(): ImageColorService {
    if (!ImageColorService.instance) {
      ImageColorService.instance = new ImageColorService();
    }
    return ImageColorService.instance;
  }

  async processFile(filePath: string, criteria: MatchingCriteria = {}): Promise<number[][]> {
    const colors = await this.getColorsExcludingBackground(filePath, criteria.excludeBackground || false);
    fs.unlinkSync(filePath);
    return colors.slice(0, 2).map(color => color.rgb());
  }

  private async getColorsExcludingBackground(filePath: string, excludeBackground: boolean): Promise<any[]> {
    return new Promise((resolve, reject) => {
      getPixels(filePath, (err, pixels) => {
        if (err) return reject(err);
        const bg = excludeBackground ? this.getBackgroundColor(pixels) : null;
        getColors(filePath).then(colors => {
          resolve(excludeBackground ? colors.filter(c => !this.isSimilar(c.rgb(), bg!)) : colors);
        }).catch(reject);
      });
    });
  }

  private getBackgroundColor(pixels: any): number[] {
    const corners = [[0, 0], [0, pixels.shape[1] - 1], [pixels.shape[0] - 1, 0], [pixels.shape[0] - 1, pixels.shape[1] - 1]];
    const colors = corners.map(([x, y]) => this.getPixelColor(pixels, x, y));
    return this.mostFrequentColor(colors);
  }

  private getPixelColor(pixels: any, x: number, y: number): number[] {
    const idx = (y * pixels.shape[0] + x) * 4;
    return [pixels.data[idx], pixels.data[idx + 1], pixels.data[idx + 2]];
  }

  private mostFrequentColor(colors: number[][]): number[] {
    const counts: { [key: string]: number } = {};
    colors.forEach(color => {
      const key = color.join(',');
      counts[key] = (counts[key] || 0) + 1;
    });
    return Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? a : b).split(',').map(Number);
  }

  private isSimilar(color1: number[], color2: number[]): boolean {
    return color1.every((v, i) => Math.abs(v - color2[i]) < 10);
  }

  analyzeColors(colors1: number[][], colors2: number[][], criteria: MatchingCriteria = {}): boolean {
    return colors1.some(c1 => colors2.some(c2 => this.isComplementary(c1, c2, criteria)));
  }

  private isComplementary(color1: number[], color2: number[], { hueDiffThreshold = 150, saturationDiffThreshold = 30, lightnessDiffThreshold = 30 }: MatchingCriteria): boolean {
    const [h1, s1, l1] = colorConvert.rgb.hsl(color1);
    const [h2, s2, l2] = colorConvert.rgb.hsl(color2);
    return Math.abs(h1 - h2) >= hueDiffThreshold && Math.abs(s1 - s2) < saturationDiffThreshold && Math.abs(l1 - l2) < lightnessDiffThreshold;
  }
}

export default ImageColorService;
