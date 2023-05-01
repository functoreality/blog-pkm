* 熟悉卢曼卡片盒笔记法的读者应该都或多或少知道，使笔记组成「网状结构」是这一笔记方法的要点之一。卢曼本人在介绍这一方法时就用了这样的表述。
	* 在 1987 年的一次采访中，卢曼提到，他的笔记不是以线性的方式组织，而是「像蜘蛛网一样的系统」，可以从任何地方进入。
		*  Luhmann, Niklas (1987): Biographie, Attitüden, Zettelkasten, in: Niklas Luhmann, Archimedes und wir. Interviews. Berlin, 125-155
			> Es gibt also keine Linearität, sondern ein spinnenförmiges System, das überall ansetzen kann. 
	* 「网络」这一表述也在《与卡片盒交流》一文（[中文翻译](https://mp.weixin.qq.com/s/_aPS2ol1DxiCFX-xfl-8yg)，[英文翻译](https://luhmann.surge.sh/communicating-with-slip-boxes)）中出现：「每一张卡片都只是一个组成部分，它的质量只取决于系统内的链接和反向链接的网络。」
* 「网状结构」对我们来说并不陌生。例如，维基百科里的超链接使各词条形成了一个网络，而学术论文也通过其相互引用关系组成了引文网络。
* 许多人认为卢曼的笔记也具有类似的结构，笔记网络由笔记卡片和它们之间的链接组成。但这种最直接的理解方式其实未必准确。
* 事实上，卢曼笔记中的链接数量其实并不多。按 Schmidt 的抽样统计，在卢曼的第一代卡片盒中，平均每张卡片上的链接数不到 0.9（20k/23k），而第二代卡片盒中这个数字仅有 0.4 左右（25k–30k/67k）。
	* 这一信息和之后的几条都来自 Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
		> The early collection ... consists of seven drawers with approximately 23,000 cards, ...
		> 
		> The later collection ... fills 21 drawers with approximately 67,000 cards. 
		> 
		> An estimate based on a sample count suggests that the first collection contains approximately 20,000 references and the second about 25,000–30,000 references of this kind, with remarkably few references between the two collections.
	* 这些（相对稀少的）链接也并非均匀分布。卢曼在一些卡片上进行了「集体引用」，其上可以列出多达 25 个的链接。相应地，更多的卡片则完全不包含任何的链接。
		> Collective references. ... A card of this kind can list up to 25 references and will typically specify the respective subject or concept in addition to the number. 
	* 有时，卢曼会在一张卡片（比如 `9/8`）上的某个词的右上角标上一个红色的数字（比如 `1`），并在其后添加的一张新卡片（比如 `9/8,1`）中补充相应的说明。这其实很像书和文章的尾注，只是把尾注的内容放进了一个单独的页面。Schmidt 实际上把这种情况也纳入了链接数目的统计。
	* 此外，卢曼的纸质笔记没有今天电子笔记的双链功能，其中的反向链接以手动补充的方式建立。也就是说，如果要表达两条笔记之间的关联，通常需要一次建立两个链接。如果能用上电子笔记的话，卢曼建立的链接可能比现在看到的要更少。
* 仅凭数量如此稀少的链接，无法组成任何意义上的「网状结构」；如果用图论的术语来说的话，这样的一个有向图根本不可能是连通的。
* 考虑到这一点，我认为有必要强调笔记序列（folgezettel）在卢曼卡片盒中的重要作用。卢曼的笔记网络实际上是由笔记序列和链接结构共同组成的，二者紧密配合，缺一不可。
	* 按照 Schmidt 的说法，卢曼的链接有时只表示对单张卡片的引用，但也有许多时候其实是引用了一串卡片的开头，而这样的一串卡片是按照笔记序列的方式组织的。
		*  Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
			> ...the references, although usually addressing individual cards, frequently only mark the beginning of a series of notes on a certain subject and, thus, the point of entry into a subject area. 
		* Schmidt 据此对卢曼「没有链接到这个网络的笔记会被遗忘」的说法进行了解读。在这里，会被遗忘的「笔记」既可以指的是单张笔记卡片，也可以是许多卡片组成的小段。即使一张卡片本身没有被任何其他卡片引用，只要它所在的笔记串中有其他的卡片被引用了，那这张卡片也不至于陷入「被遗忘」的境地。
	* 此外，卢曼建立反向链接时，有时也会利用笔记序列的结构。例如，为了表达 `21/3d18c60o9`（风险的转换）和 `7/28`（安全）这两条笔记之间的关联，卢曼实际上是在紧随前一条笔记卡片之后的 `21/3d18c60o9,1` 号卡片引用了 `7/28`，而在 `7/28,1` 号卡片中提到了 `21/3d18c60o9`。
	* 当然，「笔记序列」的说法其实不完全准确。卢曼为他的卡片引入了特殊的编号方式，而这为笔记赋予了某种树形的组织结构，其复杂度要比纯线性的「笔记序列」更高。
		* 为笔记编号也不是实现笔记序列、树形组织结构的唯一方式。我在 [[大纲语境笔记法]] 中就使用了一种不同的办法。
* 我在 [[笔记间关联方式]] 中提到，笔记序列属于空间邻近式的关联。这种关联与链接十分不同，它具有集体关联的性质，一次关联起的笔记不是两条，而是很多条。

