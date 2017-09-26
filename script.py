from pynamical import logistic_map, simulate, bifurcation_plot

pops = simulate(model=logistic_map, num_gens=100, rate_min=0, rate_max=4, num_rates=1000, num_discard=100)
bifurcation_plot(pops)

pops = simulate(model=logistic_map, num_gens=100, rate_min=3.7, rate_max=3.9, num_rates=1000, num_discard=100)
bifurcation_plot(pops, xmin=3.7, xmax=3.9)

from pynamical import cubic_map, phase_diagram_3d
pops = simulate(model=cubic_map, num_gens=3000, rate_min=3.5, num_rates=30, num_discard=100)
phase_diagram_3d(pops, xmin=-1, xmax=1, ymin=-1, ymax=1, zmin=-1, zmax=1, alpha=0.2, color='viridis', azim=330)
