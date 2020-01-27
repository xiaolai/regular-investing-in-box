# BOX 历史价格变化

```box_price_history.txt``` 是 csv 格式的文本文件，每日北京时间晚 23:58 更新一次，BTC、EOS、XIN 的价格从 Coinmarketcap 抓取获得。

更新数据之后，图片 ```box-historical-price-change.png``` 亦会同步更新

![](box-historical-price-change.png)

如果你本地安装了 Jupyter-lab，那么，可以在本地运行 ```visualization.ipynb``` 生成最新图表。

本仓库总的每日自动更新是我自己一个 linode 上的 crontab：

``` bash
58 15 * * * cd /root/regular-investing-in-box/data && /root/anaconda3/bin/python boxhistoricalprice.py && /root/anaconda3/bin/python visualization.py && cd /root/regular-investing-in-box && git pull && git add . && git commit -a -m "box historical price auto-updated and figure re-generated" && git push -u origin master
```