import pandas as pd
import cufflinks as cf
# импорт plotly и cufflinks для offline использования
import plotly.offline

cf.go_offline()
cf.set_config_gile(offline = False, world_readable = True)
