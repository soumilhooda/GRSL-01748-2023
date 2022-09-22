The DMSP OLS was designed to collect global cloud imagery using a pair of broad spectral bands placed in the visible and thermal. The DMSP satellites are flown in polar orbits and each collects fourteen orbits per day. With a 3,000 km swath width, each OLS is capable of collecting a complete set of images of the Earth twice a day. At night the visible band signal is intensified with a photomultiplier tube (PMT) to enable the detection of moonlit clouds. The boost in gain enables the detection of lights present at the Earths surface. Most of the lights are from human settlements (cities and towns) and ephemeral fires. Gas flares are also detected and can easily be identified when they are offshore or in isolated areas not impacted by urban lighting.

NGDC serves as the long term archive for DMSP, with data extending from 1992 to the present.
The archive is organized as individual orbits which are labeled to indicate the year, month, date and start time. For this project the individual orbits were processed with automatic algorithms that identify image features (such as lights and clouds) and the quality of the nighttime data. The following criteria were used to identify the best nighttime lights data for compositing:

1. Center half of orbital swath (best geolocation, reduced noise, and sharpest features).
2. No sunlight present.
3. No moonlight present.
4. No solar glare contamination.
5. Cloud-free (based on thermal detection of clouds).
6. Auroral emissions have been screened out in the northern hemisphere.

Nighttime image data from individual orbits that meet the above criteria are added into a global latitude-longitude grid (Platte Carree projection) having a resolution of 30 arc seconds. This grid cell size is approximately a square kilometer at the equator. The total number of coverages and number of cloud-free coverages are also tallied. In the typical annual cloud-free composite most areas have
twenty to a hundred cloud-free observations, providing a temporal sampling of activities such as gas flaring.

The nighttime lights product known as avg_lights_x_pct is derived from the average visible band digital number (DN) of cloud-free light detections multiplied by the percent frequency of light detection. The inclusion of the percent frequency of detection term normalizes the resulting digital values for variations in the persistence of lighting. For instance, the value for a light only detected half the time is discounted by 50%. Note that this product contains detections from fires and a variable amount of background noise. 
