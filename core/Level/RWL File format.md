# Slug parser

parses .rwl files into dict and vise versa

you would need it: https://docs.google.com/document/d/1zcxeQGibkZORstwGQUovhQk71k00B69oYwkqFpGyOqs/edit#heading=h.7xts9mnasx5f

reading of geo, tiles, and anything matrix related goes from left to right, top to bottom

# Specification:

RWL file is a zip archive containing files for each one of the editors

```
Level.rwl
├ info      - all information about level
├ geometry  - level geometry
├ tiles     - level tiles
├ light.png - light image
├ props     - level props
├ cameras   - level cameras
```

# info

1. RWL file version
2. level dimensions(width;height)
3. extra tiles(left;top;right;bottom)
4. light(0 or 1), angle and flatness(light;angle;flatness)
5. tile seed
