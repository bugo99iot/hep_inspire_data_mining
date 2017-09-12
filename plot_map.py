"""import matplotlib.cm
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

fig, ax = plt.subplots(figsize=(10,20))

# resolution: c, l, i, h, f or None
m = Basemap(resolution='c',
            projection='merc',
            lat_0=54.5, lon_0=-4.36,
            llcrnrlon=-6., llcrnrlat= 49.5, urcrnrlon=2., urcrnrlat=55.2)

m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
m.drawcoastlines()

"""

import matplotlib.cm
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

fig, ax = plt.subplots(figsize=(10,20))

#westlimit=-24.66; southlimit=34.96; eastlimit=39.77; northlimit=66.65
# resolution: c, l, i, h, f or None

map = Basemap(resolution='c',
            projection='merc',
            lat_0=54.5, lon_0=-4.36,
            llcrnrlon=-24.66, llcrnrlat= 34.96, urcrnrlon=39.77, urcrnrlat=66.65)

map.drawcountries(linewidth=0.7, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

#x, y = map(0, 0)

#map.plot(x, y, marker='D',color='m')

plt.show()
