import matplotlib.pyplot as plt
import numpy as np
from Models.src.core import neutral_iono_parameters
import datetime as dt

def plot_local_conductivies(
        ax, 
        nu, 
        alts, 
        step = 50
        ):
    
    name = "Condutividades locais"
    units = "mho/m"
    
    if nu.name == "perd":
        symbol = "$\sigma_{P}$"
    elif nu.name == "hall":
        symbol = "$\sigma_{H}$"
    else:
        symbol = "$\sigma_{0}$"
        
    ax.plot(nu, alts,
            lw = 1, label = symbol)
    
    ax.legend(loc = "upper right")
    
    ax.set(
        xscale = "log", 
        yticks = np.arange(
            min(alts), 
            max(alts) + step, 
            step
            ),
        
        ylim = [min(alts), max(alts)],
        xlim = [1e-14, 1e7],
        xlabel = f"{name} ({units})",
        ylabel = "Altitude (km)"
        )
    return ax

def plot_local_ratio_conductivities():
    
     fig, ax = plt.subplots(
         dpi = 300, 
         ncols = 2,
         sharey = True
         )

     dn  = dt.datetime(2013, 1, 1, 12, 0)
     
     df = neutral_iono_parameters(
        dn  = dn, 
        hmin = 50, 
        hmax = 400,
        mass = "effective")
     
     
     ax[1].plot(df["hall"] / df["perd"],  df.index)
     ax[1].set(
         xlim = [-2, 100], 
         xlabel = "$\sigma_H / \sigma_P$"
               )
     
     plot_local_conductivies(
            ax[0], 
            df["perd"], 
            df.index
            )
    
     plot_local_conductivies(
            ax[0], 
            df["hall"], 
            df.index
            )
    
     ax = plot_local_conductivies(
            ax[0], 
            df["par"], 
            df.index
            )
     
     fig.suptitle(dn.strftime("%d/%m/%Y %H:%M (UT)") +
                  " - São Luís")
     
     return fig
     

from utils import save_plot     
plot_local_ratio_conductivities()