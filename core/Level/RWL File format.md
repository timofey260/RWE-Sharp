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

First line of info file is RWL file version

Second line is level dimensions(width;height)

Third line is extra tiles(left;top;right;bottom)

Forth line is light(0 or 1)

Fifth line is tile seed
