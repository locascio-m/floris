# Copyright 2021 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# See https://floris.readthedocs.io for documentation

import matplotlib.pyplot as plt
import numpy as np

from floris.tools import FlorisInterface
from floris.tools.visualization import visualize_cut_plane


# Initialize the FLORIS Interface, `fi`.
# For basic usage, the FLORIS Interface provides a simplified
# and expressive interface to the simulation routines.

fi = FlorisInterface("../example_input.yaml")
solver_settings = {
    "type": "flow_field_grid",
    "flow_field_grid_points": [200,200,7]
}
fi.reinitialize(solver_settings=solver_settings)

yaw_angles = np.zeros((1,1,3))
fi.floris.farm.yaw_angles = yaw_angles

# Do the wake calculation
fi.floris.solve_for_viz()

# At this point, the flow field data is generated and
# stored in memory. Now, use the visualization components
# in `fi` to get slices of the flow field and generate plots.

horizontal_plane = fi.get_hor_plane()
cross_plane = fi.get_cross_plane()
y_plane = fi.get_y_plane()

fig, ax = plt.subplots()
visualize_cut_plane(horizontal_plane, ax=ax)

fig, ax = plt.subplots()
visualize_cut_plane(cross_plane, ax=ax)

fig, ax = plt.subplots()
visualize_cut_plane(y_plane, ax=ax)

plt.show()
