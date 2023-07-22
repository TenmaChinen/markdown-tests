import dj_setup

from classic_models.models import Office, Employee, Customer, Order, ProductLine, Product, OrderDetail, Payment
from pandas import DataFrame, set_option
from tabulate import tabulate
from utils import df_to_image
import exercise_queries as eq

set_option('display.max_columns', 1000)
set_option('display.width', 2000)

for idx in range(1,45):
    func = getattr( eq, f'get_exercise_{idx}' )
    df = func()
    
    print(idx)
    img_pil = df_to_image(df=df)
    file_name = f'../images/sample_{idx:02d}.png'
    img_pil.save(file_name)
