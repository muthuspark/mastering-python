import cProfile
import pstats

cProfile.run('my_function(1000000)', 'profile_results')
p = pstats.Stats('profile_results')
p.sort_stats('cumulative').print_stats(20) # Shows top 20 functions by cumulative time.