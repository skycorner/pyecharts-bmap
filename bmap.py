# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:44:00 2019

@author: Administrator
"""

from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType
from pyecharts.charts import BMap
'''
def test_geo():
    city = '长沙'
    g = Geo()
    g.add_schema(maptype=city)
    
    # 定义坐标对应的名称，添加到坐标库中 add_coordinate(name, lng, lat)
    g.add_coordinate('湖南省长沙市宁乡市横市镇藕塘', 112.21369756169062, 28.211359706637378)
    g.add_coordinate('湖南省长沙市雨花区跳马镇仙峰岭', 113.16921879037058, 28.039877432448428)
    g.add_coordinate('湖南省长沙市长沙县黄花镇新塘铺长沙黄花国际机场', 113.23212337884058, 28.19327497825815)
    
    # 定义数据对，
    data_pair = [('湖南省长沙市雨花区跳马镇仙峰岭', 10), ('湖南省长沙市宁乡市横市镇藕塘', 5), ('湖南省长沙市长沙县黄花镇新塘铺长沙黄花国际机场', 20)]
    
   
    # Geo 图类型，有 scatter, effectScatter, heatmap, lines 4 种，建议使用
    # from pyecharts.globals import GeoType
    # GeoType.GeoType.EFFECT_SCATTER，GeoType.HEATMAP，GeoType.LINES
    
     # 将数据添加到地图上
    g.add('', data_pair, "scatter", symbol_size=5)
    # 设置样式
    g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    # 自定义分段 color 可以用取色器取色
    pieces = [
        {'max': 1, 'label': '0以下', 'color': '#50A3BA'},
        {'min': 1, 'max': 10,  'label': '1-10', 'color': '#3700A4'},
        {'min': 10, 'max': 20, 'label': '10-20', 'color': '#81AE9F'},
        {'min': 20, 'max': 30, 'label': '20-30', 'color': '#E2C568'},
        {'min': 30, 'max': 50, 'label': '30-50', 'color': '#FCF84D'},
        {'min': 50, 'max': 100, 'label': '50-100', 'color': '#DD0200'},
        {'min': 100, 'max': 200, 'label': '100-200', 'color': '#DD675E'},
        {'min': 200, 'label': '200以上', 'color': '#D94E5D'}  # 有下限无上限
    ]
    #  is_piecewise 是否自定义分段， 变为true 才能生效
    g.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces),
            title_opts=opts.TitleOpts(title="{}-店铺分布".format(city))
            )
    return g

g=test_geo()
# 渲染成html, 可用浏览器直接打开
g.render('test_render.html')
'''

# -*- coding: utf-8 -*-
# 导入必要模块
import pandas as pd
from sqlalchemy import create_engine



def test_bmap():
    b = BMap()
    b.add_schema(baidu_ak='iMplFNfYyAf4e7EleegtObtcOZdliriG',center=[116.395645,39.929986],zoom=9)
    
    # 定义坐标对应的名称，添加到坐标库中 add_coordinate(name, lng, lat)
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')

    # 查询语句，选出employee表中的所有数据
    sql = '''select * from 4sstore_beijing;'''
    # read_sql_query的两个参数: sql语句， 数据库连接
    df = pd.read_sql_query(sql, engine)
    data_pair=[]
    for index,row in df.iterrows():
        b.add_coordinate(row['name'], float(row['lng']),float(row['lat']))
        data_pair.append((row['name'], None))
       
    # Geo 图类型，有 scatter, effectScatter, heatmap, lines 4 种，建议使用
    # from pyecharts.globals import GeoType
    # GeoType.GeoType.EFFECT_SCATTER，GeoType.HEATMAP，GeoType.LINES
    
     # 将数据添加到地图上
    b.add('bmap', data_pair, "scatter" ,symbol_size=5)
    # 设置样式
    b.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    b.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_piecewise=False),
            title_opts=opts.TitleOpts(title="北京4s店分布")
            )
    return b

b=test_bmap()
b.render('test_render2.html')
