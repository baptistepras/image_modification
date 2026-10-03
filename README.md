# Image Modification

Pure Python functions to edit PPM images, with no external library: color inversion, grayscale, bars over the image, overlay with a transparent color key, scaling, mosaic and rotation. Each function comes with its tests.

## Usage

```bash
python filters.py
```

`main()` reads `puppy.ppm`, applies every filter and writes the results next to it (`puppy_gray.ppm`, `puppy_mosaic.ppm`, and so on). Any PPM image works in place of the example.

## License

MIT, see [LICENSE](LICENSE).
