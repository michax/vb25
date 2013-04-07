'''

  V-Ray/Blender

  http://vray.cgdo.ru

  Author: Andrey M. Izrantsev (aka bdancer)
  E-Mail: izrantsev@cgdo.ru

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.

'''


''' Blender modules '''
import bpy
from bpy.props import *


TYPE= 'MATERIAL'
ID=   'MtlBakeStats'
PID=   120

NAME= 'Bake Stats'
UI=   "Bake"
DESC= "MtlBakeStats settings."

PARAMS= (
    'bake'
)


def add_properties(rna_pointer):
    class MtlBakeStats(bpy.types.PropertyGroup):
        pass
    bpy.utils.register_class(MtlBakeStats)

    rna_pointer.MtlBakeStats= PointerProperty(
        name= "MtlBakeStats",
        type=  MtlBakeStats,
        description= "V-Ray MtlBakeStats settings"
    )

    MtlBakeStats.use= BoolProperty(
        name= "Use bake render options",
        description= "Use bake render options",
        default= False
    )

    MtlBakeStats.uv= StringProperty(
        name= "Bake uv",
        description= "UV used for bake. In most cases it's second one.",
        default= ""
    )

    MtlBakeStats.override_resolution = BoolProperty(
        name= "Override resolution",
        description= "Override scene resolution",
        default= False
    )

    MtlBakeStats.resolution_x= IntProperty(
        name= "X",
        description= "X",
        min= 2,
        max= 16384,
        step= 128,
        default= 1024
    )
    MtlBakeStats.resolution_y= IntProperty(
        name= "Y",
        description= "Y",
        min= 2,
        max= 16384,
        step= 128,
        default= 1024
    )