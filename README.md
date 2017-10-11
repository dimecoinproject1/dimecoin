



**dimecoin update**
=========

----


![dimecoin](https://cdn.pbrd.co/images/GNQe2gQ.png)




-----


<ul>
<li><a href="#dimecoin-update">dimecoin update</a><ul>
<li><a href="#wallet-at-github">Wallet at Github</a></li>
<li><a href="#full-windows-compile-including-the-whole-source-code-and-the-qt">Full Windows compile including the whole source code and the qt</a></li>
<li><a href="#changes">Changes</a></li>
<li><a href="#source-used">Source used</a></li>
<li><a href="#bootstrap">bootstrap</a><ul>
</ul>
</li>
<li><a href="#remaining-issues">Remaining Issues</a><ul>
<li><a href="#wallet-background">Wallet background</a></li>
<li><a href="#dimecoinconf">dimecoin.conf</a></li>
<li><a href="#addnodes">Addnodes</a></li>
<li><a href="#setgenerate">Setgenerate</a></li>
<li><a href="#to-do">To do</a></li>
</ul>
</li>
</ul>


-----





*Another dimecoin wallet for you, but with some changes made.(no mandatory swap necessary of course)*


-----



Wallet at Github
-------------


[Updated Dimecoin-qt Download](https://github.com/dimecoinproject1/dimecoin1.7-qt/raw/master/Dimecoin-qt.zip)


-----

Full Windows compile including the whole source code and the qt
-------------

[Full Windows Compile](https://github.com/dimecoinproject1/Complete-Windows-Compile)


-----

Changes
-------------

- Hopefully the **sending limit has been lifted** so you can send as many coins as you desire to send.

- The rpc call **getnetworkhasps** has been added

- A simple background image has been added to the wallet

- **I added some nodes** that you can hopefully connect to (I hope they are reliable enough)


- I Changed the **pro** file to a **qt-pro** file

- Some minor changes made to dimecoin-qt.pro, including the path set, and updating to **mgw49-mt-s-1_55**

- **Since no Windows dependencies are in the original source, I put those necessary to compile on Windows in. They remain there, but I have commented them out (lines 33-43). To compile on Windows these simply need unchecking (remove the # on each of them)**

- Updated to Protocol version **70003**

- Updated to Dimecoin client version **1.7.0.1**

- I changed the horrible old icons and used the logo from dimecoin 1.5



-----

Source used
-------------

The source used was the original by Antcoin at: 

https://github.com/dimecoinproject/dimecoin


-----




bootstrap
=========



> file: **bootstrap.dat**
> 
> The bootstrap contains block data up to approximately block 2,448,000 (2 million, four hundred and forty eight thousand). It was created on the 9th October 2017. 

> You should unzip the download first. The contents, boostrap.dat, should be placed in your dimecoin folder located at %appdata% (Roaming). Remove all items in the folder first, or simply rename the folder dimecoin1, and make a new folder called dimecoin. Copy paste the bootstrap to  the empty folder, and add a dimecoin.conf. 

> Then start your dimecoin-qt and it will start importing blocks from the bootstrap. The process is somewhat faster than downloading from the blockchain. 

> Blocks produced after the bootstrap, will automatically begin to download from the blockchain when the bootstrap is finished, from 9th October, 2017.

> If you have wallet.dat with dimecoin in it, when the wallet is fully synched, stop dimecoin-qt, wait a minute or two to be sure the bloated client has really closed (you can check in Task Manager), remove wallet.dat, and copy paste your own wallet.dat into the new folder.

> **NB: Always copy paste (do not cut paste) in case something goes wrong. You will then still have a fresh unharmed copy of your wallet.dat.**
> 
> [Dimecoin Bootstrap](https://mega.nz/#!5nB1yYzb!DDRQAY8e5jOboZ23qgQ1OtKUlYFx82xEkmoipRMVkTU) (1 GB)
> 
> Hosted at Mega-NZ
> 
>


-----

**Remaining Issues**
=======================


**Dimecoin has a huge bloated chain, and you should give the wallet a higher priority in Windows Task Manager. If not, you face the prospect of the wallet becoming unresponsive or not even opening.**

- Somebdy with the know-how and time ought to make an **Electrum version** of the wallet!!


-----

Wallet background
-------------


Simple



![dime bkg.png](https://cdn.pbrd.co/images/GNQar5l.png)


-----



dimecoin.conf
--------------------

>- rpcuser=dimecoinrpc
>- rpcpassword=LongShitHereRepeatwithNum838s
>- rpcallowip=127.0.0.1
>- daemon=1
>- server=1
>- rpcport=11930
>- port=11931


-----

Addnodes
--------------------

Go to https://chainz.cryptoid.info/dime/#!network

You will find 70 or so nodes to use in your dimecoin.conf, as such:

> addnode=111.92.56.73
> 
> addnode=111.92.57.239



You can also visit [www.dimecoin.rocks](http://www.dimecoin.rocks/) where there is a copy of peers.dat from a fully synched wallet, which may help you connect to more nodes, as the information in peers.dat will already have a list of reliable connections to seek out.



-----

**Active nodes 11 October**

You may notice a pattern between these nodes that are active at this moment, and future data reported by [Chainz Explorer](https://chainz.cryptoid.info/dime/#!network), in which case you can consider matching nodes as reliable to add to your dimecoin.conf. I have put them down as addnodes. 

    addnode=45.50.102.111:11931
    addnode=177.85.98.203:11931
    addnode=107.189.41.253:11931
    addnode=5.9.112.62:11931
    addnode=91.121.217.70:11931
    addnode=138.201.221.88:11931
    addnode=93.115.28.30:38858
    addnode=217.175.119.125:20653
    addnode=184.164.129.202:62204
    addnode=51.254.45.117:48096
    addnode=71.3.103.242:61268
    addnode=144.217.71.144:43612
    addnode=35.197.25.60:56010
    addnode=24.12.252.213:50220
    addnode=151.80.166.130:54656
    addnode=46.165.221.81:41380
    addnode=145.87.231.247:50636
    addnode=73.167.158.80:50783
    addnode=194.67.217.176:46986
    addnode=37.187.24.211:13551
    addnode=[2001:0:9d38:90d7:89d:2347:6ea8:1808]:11931
    addnode=59.98.152.17:21353
    addnode=195.24.73.169:62954
    addnode=93.41.3.173:24920
    addnode=188.134.72.213:35725
    addnode=46.216.6.148:11931 
    addnode=5.189.179.102:55287
    addnode=5.100.92.30:58658
    addnode=5.189.179.102:55287


-----


Setgenerate
--------------------

I left **setgenerate** in as an rpc call, as it possibly useful. However, this means the qt will always get flagged for bitcoin miner. It is a false positive, and everyone should know that by now.

-----

To do
--------------------

1. Change the background image to the dimecoin planets image on the splash.
2. Update the logo when the new one is available (as reported by [dimecoin.rocks](http://www.dimecoin.rocks/).


-----

