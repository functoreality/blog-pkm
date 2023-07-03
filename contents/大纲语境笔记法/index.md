---
layout: folded_post
title: "大纲语境笔记法"
date: 2023-07-03 +0800
categories: jekyll update
---

* 首先声明，这篇文章中将要介绍的笔记方法主要面向理论文章阅读、思考工具的需求，参见 [笔记的不同目的](../笔记的不同目的/)。对于其他需求（比如狭义的知识管理），我不排除这种方法也有其参考价值，不过这不作为本文的主要目的。
* 基于我目前所了解到的信息，我认为这里将要描述的方法在精神上较为接近卢曼在其二代卡片盒中所使用的方法。
* <input type="checkbox" name="fchk" id="fold3"><label for="fold3">不过我并没有沿用「卡片盒笔记法」的称呼，而是采用了一个稍不一样的名字。这当中有多个方面的考量。</label>
	* <input type="checkbox" name="fchk" id="fold4"><label for="fold4">第一，卢曼所用方法在目的、组织方式、形式与内容的对应方式、工具实现、整体工作流程等各个方面都有十分丰富的内容。至于其中哪些元素应该视作组成「卡片盒笔记法」的关键，不同人的理解相去甚远。</label>
		* 这种理解上的差异性使得「卡片盒笔记法」这个概念已经在某种意义上成了忒修斯之船。此时若贸然沿用「卡片盒笔记法」这个称呼，将带来不可避免的语言模糊性。
	* <input type="checkbox" name="fchk" id="fold6"><label for="fold6">第二，本文所理解的卡片盒方法与当前互联网上绝大多数讨论中的确实有很大不同。为避免可能的误解，我使用了一个新名称，这并不代表我认为这是自己独创的方法。</label>
		* 许多人对卡片盒笔记法的了解来自 Ahrens 的《卡片笔记写作法》一书，这大概是造成这一现象的主要原因。
		* 而 Ahrens 所描述的方法与卢曼的方法有许多关键的不同，我在 [笔记的不同目的](../笔记的不同目的/) 中已经对此进行了部分讨论。
	* 第三是出于严谨性的考量。必须承认，我自己到目前为止也还没有完全理解这一方法；此外卢曼二代卡片盒的文字版本还需要较长的时间才会完全公布，在这以前，我很难对卢曼方法的具体细节进行更细致的考证。
	* 第四，我仍希望为自己保留一些探索的空间。至少，我们的笔记更多采用电子而非纸质的方式记录，这就带来了许多潜在的改进可能。
	* 第五，「大纲语境笔记法」这个名称看起来还算贴切，它强调了这一方法的关键部分：现在笔记的形式将是「大纲」（而非纸质的卡片），而「语境」则点明了这一形式为笔记内容服务的具体方式。
* <input type="checkbox" name="fchk" id="fold12"><label for="fold12">先强调一下「语境」在笔记中的重要性，特定的笔记必须放在特定的语境中，才具有完整的价值。</label>
	* Andy Matuschak 在他的博客的 [这篇短文](https://notes.andymatuschak.org/z7DvEiUpF6dYkFGbpZZTBKQVM9jjNnx8D8Xzu) 中强调，好的文段并非孤立存在，它依赖于特定的叙述方式，并需要放在适当的语境当中。他据此对许多笔记软件中「块嵌入」功能的实用性表达了怀疑。
	* <input type="checkbox" name="fchk" id="fold14"><label for="fold14">Kimbro 也认为，在笔记中记录想法的时候，必须标明这一想法产生的语境，它在某些方面甚至「比想法本身更重要」。</label>
		* Kimbro 认为，一个新想法「不是凭空出现的，而是在语境中出现的」。如果我们没有标明这一语境，那么在下次回看这个想法的时候，我们将需要耗费更多的时间、精力来「辨认这个想法，并识别出（它所产生的）语境」。
		* <input type="checkbox" name="fchk" id="fold16"><label for="fold16">Kimbro, Lion. (2003). How to Make a Complete Map of Every Thought You Think[J]. </label>
			> So the “hint” describes the context. This is VERY IMPORTANT! The context is fresh in your mind when you get the thought! It would take a while to recognize the thought, and then identify the context, if you didn’t. 
			> 
			> Besides, the thought is MOST useful in the ORIGINAL context, 95the time. And your hint- that’s going to be USED. In some respects, it’s EVEN MORE IMPORTANT THAN THE THOUGHT ITSELF! 
* <input type="checkbox" name="fchk" id="fold20"><label for="fold20">许多介绍卢曼方法的材料认为，一条笔记应该是自成一体的，可以被单独理解。但是这种要求实际上造成了一种矛盾的局面，我们很难在充分地记录语境、保持笔记的原子性二者之间取得平衡。</label>
	* 为了保持笔记的原子性，我们难以在笔记中进行完整的说明、记录这一内容所产生的语境，而语境记录的不充分性将导致笔记价值的降低。
	* 另一方面，即使只对这一语境进行部分的说明，也会干扰这条笔记的原子性，导致一条笔记的粒度无法做到足够的细，从而提高了重读、重用时的认知成本。
	* <input type="checkbox" name="fchk" id="fold23"><label for="fold23">此外，许多条不同笔记可能是在相同或相近的语境下产生的，为这些笔记都分别补上相应的背景说明，则要做很多重复功，也为笔记的后续使用带来了不便。</label>
		* 如果考虑重读一批这样的笔记，我们将需要分辨笔记的内容中哪些是共享的背景说明，哪些是某条笔记特有的东西。这同样会带来不必要的认知成本。
		* 若是再考虑输出的需求，使用这样的卡片笔记来组装文章，不同卡片中以这种方式引入的大量重复内容将成为严重的干扰因素，很容易使最后写出的内容显得「啰唆」，也不易保持逻辑的连贯性。
	* 实践中也有许多人遇到了「原子化单位应该选取多大」的问题，似乎两条笔记既有合并成一条的道理，也有保持其各自独立性的道理。
* <input type="checkbox" name="fchk" id="fold27"><label for="fold27">而卢曼的一张卡片实际上不能用「自成一体」来描述，也即它尽管是笔记管理（添加、链接）中的原子化单位，但却并非传统意义上的「一条笔记」，无法独立于特定的上下文语境而存在。</label>
	* <input type="checkbox" name="fchk" id="fold28"><label for="fold28">卢曼在《与卡片盒交流》中提到：「原本连续的文本经常被数百张插入的新卡片打断；但如果系统地处理编号，就很容易找回原有文本的全貌。」</label>
		*  这一信息主要来自文章的 [英文翻译](https://luhmann.surge.sh/communicating-with-slip-boxes)：
			> The disadvantage is that the originally continuous text is often broken up by hundreds of intermediate slips. But if we systematically number the papers, we can find the original textual whole easily. 
		* <input type="checkbox" name="fchk" id="fold31"><label for="fold31">Schmidt 也对此进行了确认，他在卢曼的卡片盒中多次发现了上百张的卡片，它们「后来被插入到最初在相关主题上同时创建的、两张连续的卡片之间」。</label>
			*  Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
				> ...in some cases, we also find several 100 cards that were later inserted between what had ­initially been two consecutive cards created at the same time on a related subject. 
	* 注意这句话中透露了一个重要的信息：卢曼向他的卡片盒中添加一段连续内容的时候，没有把它们放在同一张卡片之中，而是将这些文字拆成了若干小段，分别写在几张连续编号的卡片上。
	* 有人可能觉得这仅仅是纸质笔记时代的物理限制，卢曼的一张卡片不够大，写不下所有内容。但这种说法其实是站不住脚的；如果真是如此，那卢曼完全可以把这几张写着连续内容的卡片当成一整张「连体卡片」，没必要、也不应该向其中再插入新的内容。
	* 因此，必须指出的是，卢曼使用拆分连续文本的方式来保证卡片内容的简短性，这本身是一种十分重要的技巧。Daniel Lüdecke 在 [这篇文章](https://strengejacke.wordpress.com/2015/11/01/you-underestimate-the-power-of-the-dark-folgezettel/) 中同样对此进行了强调。
	* <input type="checkbox" name="fchk" id="fold37"><label for="fold37">关于这种拆分、从中插入新卡片做法的意义，读者可以直接看看这篇文章的组织方式，文中有许多内容是默认折叠的。如果这些折叠部分的内容可以在日后随时补充，它所带来的好处相信读者能够理解。</label>
		* 不过其实本文中折叠的用法其实已有些拘束，毕竟这是呈现给读者看的完整文章。实际使用中的这种插入可以更加灵活，根据自己的想法来进行即可。
	* 而至于插入的新卡片数量为何能达到数百张之多，后文讨论组织上的树形结构时将进行更多解释。
* <input type="checkbox" name="fchk" id="fold40"><label for="fold40">在这一方面，卢曼的卡片编号承担起了记录卡片原始语境的重要任务，其功能绝不是「永久地标识每条笔记」就能概括的。</label>
	* 此外，编号的数字增长（如从 `1a` 到 `1b`）与位数增加（如从 `1a` 到 `1a1`）对应的含义并不相同。不过这点其实并不需要专门解释，只要理解了卢曼编号与大纲笔记的对应关系（它们都是树形结构），再看看这篇文章的组织方式，就立刻能够理解了。它实际上是十分自然的做法。
* <input type="checkbox" name="fchk" id="fold42"><label for="fold42">若考虑卡片盒笔记法的电子实现，首先需要确定纸质卡片在电子笔记中的对应物。最符合直觉的方式是使用一个单独的文件（或者说页面），这很大程度上源于二者形式上的相似性。但如果从功能（或者目的）的角度考虑，这不见得是最高效的；我们完全可以把所有笔记都放进同一个页面之中。</label>
	* 使用纸质笔记时，我们很难在两行原本相邻的文字之间再插入大量的新内容。要实现这一点，我们只好将这些文字分别写在不同的卡片上。但是这种麻烦在电子笔记中并不存在，我们插入新内容的过程本来就十分方便，在笔记的任何位置都能进行。
	* 卢曼使用独立卡片的另一个原因是它可以作为链接的单位。许多电子笔记软件都引入了「块引用」的功能，可以直接建立指向某一行文字的链接；这实际上允许我们将电子笔记中的文本行作为卢曼式纸质卡片的替代品。
	* 另外，卢曼的卡片只在一面上写了字，并且紧密地排列在他的木盒中，这允许他快速地翻看一系列连续的卡片。若将笔记内容分散在电子笔记的不同页面中，这样的「翻看」通常会更加麻烦。但若将它们紧凑地写在同一个页面里，「翻看」只会更加简单；事实上，我们甚至经常能免掉「翻」的步骤，只需要「看」就可以了。
	* <input type="checkbox" name="fchk" id="fold46"><label for="fold46">如果说双链笔记给我们带来了笔记管理「只用一个文件夹」的可能性的话，那么这篇文章将进一步提供「只用一个页面」的可能性。</label>
		* 当然，这种可能性主要是理论上的。考虑到软件性能、处理历史遗留问题等多方面的因素，我们仍然可以划分出几个不同的页面，只要心里明白这种划分本身不具有必然性就可以了。
* <input type="checkbox" name="fchk" id="fold48"><label for="fold48">如果进一步考虑大纲笔记，那么大纲所代表的树形组织结构正好成了卢曼式卡片编号的完美替代品，我们连编号的过程都免去了。</label>
	* 这个博客里的文章（包括这一篇）就是按着大纲的形式组织的。大纲笔记软件并不是什么新东西，Workflowy 和幕布就是比较经典的例子，而双链软件中的 Roam Research、Logseq 等也属于大纲型的笔记软件。
	* 大纲结构与卢曼卡片编号的具体对应方式其实不难理解，很多人都自己意识到了这一点。如果有读者希望了解这一对应关系的具体细节，可以看看 [笔记间关联方式](../笔记间关联方式/)，我在讨论空间邻近关系的时候，就解释了「卢曼所用的笔记序列可以看成大纲笔记在纸质时代的物理实现」。
* <input type="checkbox" name="fchk" id="fold51"><label for="fold51">但我们的使用方式也将不同于传统意义上的大纲笔记：组织上的树形结构现在不再表示内容（或者说逻辑）上的树形结构，它面向的是语境的承接与延续性，新増的内容只需从已有笔记的语境中自然引申出来即可，无需保持任何意义上的整体结构。</label>
	* <input type="checkbox" name="fchk" id="fold52"><label for="fold52">例如，在卢曼二代卡片盒的「功能主义」条目下，随着树状层级的不断加深，卢曼依次讨论了这些内容：功能概念、功能分析的参考单位、持续存在条件的概念、功能问题的概念、期望的概念、社会认同、真诚、秘密。</label>
		*  Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
			> For instance, when we look up the keyword ‘functionalism’, we find the following sequence of terms: concept of function – unit of reference of functional analysis – concept of conditions for continued existence – concept of functional problem – concept of expectations – social identity – sincerity – secret.
	* 这个例子并不难理解。对「社会认同」的讨论将涉及到许多的方面，其中就包括「真诚」。而当我们对「真诚」进行进一步的展开讨论时，也就自然地谈到了「秘密」。
	* 当然，「秘密」这个话题已经和之前的「社会认同」的距离比较远了，和再之前的「功能主义」更是没多少相关性。
	* 但是，这仍是卡片盒里最适合讨论「秘密」的位置，因为它的上一层正在进行关于「真诚」的讨论，而将「秘密」有关的内容放在这里的讨论语境中显得尤其自然。
	* <input type="checkbox" name="fchk" id="fold58"><label for="fold58">Schmidt 对此评论说，这种做法的结果是「一系列卡片与最初的主题越来越远」，笔记实现了「向内的生长」。</label>
		*  Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
			> This method could be applied again to the card that had been inserted, the result being a sequence of cards leading farther and farther away from the initial subject, which enabled the collection to grow ‘inwardly’. 
	* <input type="checkbox" name="fchk" id="fold61"><label for="fold61">这样的做法也使得卢曼卡片盒的生长没有深度的限制，可以产生深达 13 层的笔记（编号 `21/3a1p5c4fB1a`，保密性）。</label>
		* 而对于电子大纲笔记而言，其中笔记的粒度实际上通常比卢曼的更小（这也是电子笔记的优势，我们无需控制卡片的总数，可以写更细粒度的笔记），因此这里的层数完全可以更深。我自己已经做好了达到 20 层以上深度的准备。
	* 而之前提到的相邻卡片中插入数百张新卡片的现象，也由此得到了解释。为了对其中一张卡片的内容进行展开讨论，卢曼添加了几张卡片，而其中有的卡片又可以展开讨论。这样的展开不会受到任何限制，几百张新插入的卡片最终就这么产生了。
	* 在这一方面，这篇文章的组织方式并不是一个很好的例子。我自己的笔记里其实有非常多发散讨论的内容，不过为了确保文章主题的一致性，我在写文章时把这些不那么相关的部分都截掉了，它们没有呈现在读者眼前。
* <input type="checkbox" name="fchk" id="fold65"><label for="fold65">进一步，由于这种树形结构仅在组织上、而不在内容上成立，它对我们查找特定的笔记不总是有帮助。卢曼据此制作了「索引笔记」，作为他的笔记系统的入口。</label>
	* 在《与卡片盒交流》一文（[中文翻译](https://mp.weixin.qq.com/s/_aPS2ol1DxiCFX-xfl-8yg)，[英文翻译](https://luhmann.surge.sh/communicating-with-slip-boxes)）中，卢曼写道：「考虑到卡片盒没有系统的顺序，我们必须规范重新发现笔记的过程，因为我们不能依靠对数字的记忆。」
	* 卢曼的索引笔记中列出了一系列的关键词，每个关键词之后给出了少量的链接，它们指向卡片盒里的具体笔记。
	* <input type="checkbox" name="fchk" id="fold68"><label for="fold68">按 Schmidt 的说法，这个关键词索引并不要求提供所有相关笔记的完整列表，通常只列出可找到这个术语的一到三个位置。在那以后，卢曼可以通过笔记之间建立的大量链接，快速找到其他的相关笔记。</label>
		*  Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
			> Contrary to the subject index of a book, the file’s keyword index makes no claim to providing a complete list of all entries in the collection that refer to a specific term. 
			> Rather, Luhmann typically listed only one to three places where the term could be found in the file, the idea being that all other relevant entries in the collection could be quickly identified via the internal system of references. 
			> By contrast, the large number of keywords listed in the keyword index indicates that this index was at least intended to meet the standard of completeness.
		<!-- * 卢曼只试图保证所有可能的关键词都在其中出现了（二代卡片盒共有 3200 个关键词），而并不打算在这里给出所有的相关链接。 -->
	* 例如，卢曼二代卡片盒索引中「风险的一般概念（Risiko，Riskanz allg.）」这个关键词只引用了 `21/3d18c60o9` 这一张卡片，而紧随其后的 `21/3d18c60o9,1` 卡片是一条枢纽笔记，上面写着 14 个链接。
	* 在这一方面，[MOC的组织](../MOC的组织/) 这篇文章仍有一定的参考价值（尽管作为我旧有认知的见证，其中不恰当地假定了各条笔记是自成一体的）。我们可以让索引中的关键词条目指向一些（可能位于笔记深处的）MOC，让它们充当我们查找笔记的跳板。
	* <input type="checkbox" name="fchk" id="fold76"><label for="fold76">由于树形结构只在于组织上而不在内容上，相近主题的笔记可能分散在笔记中十分不同的位置，因此这里的 MOC 中涉及的链接也常常是远距离的。</label>
		* 例如，上面卢曼的例子提到的 14 个链接中，除了有 3 个引用了位置较接近的笔记（比如 `21/3d18c60o21`）以外，其他链接都指向着卡片盒中距离非常遥远的位置，绝大部分（10 个）也并不以 `2` 作为编号的开头。
	* <input type="checkbox" name="fchk" id="fold78"><label for="fold78">另外，特定关键词所指向的笔记有时也并非对这一关键词本身的解释。</label>
		* 例如，上面提到的 `21/3d18c60o9` 这张卡片的开头已经表明，其中所讨论的内容其实是「风险的转换（Transformation von Risiko）」，而不是指向它的关键词「风险的一般概念」。
		* 这其实并不奇怪，因为卢曼的卡片都是在（由已有卡片笔记所形成的）特定的语境下写出来的，其本身的重点并不在于对某个一般性的概念或问题展开讨论。
		* 按照我自己的理解，这种做法也在一定程度上增强了笔记系统作为「惊喜生成器」的能力。当我们带着问题，从索引笔记中的某个关键词进入时，所看到的内容往往能启发我们从一个不太一样的角度来思考脑海中的那个问题。
		* <input type="checkbox" name="fchk" id="fold82"><label for="fold82">我也在自己的笔记系统中尝试了类似的做法。例如，我的索引笔记中「公众人物」关键词所指向的笔记就在探讨「网络科学中枢纽节点效应在社会网络中的可能表现」，其中甚至根本没有出现「公众人物」这个词。</label>
			* 当然，我的笔记中并不需要把「网络科学中枢纽节点效应在社会网络中的可能表现」这一长串文字完整地写下来。这是因为它是承接着前几条笔记的语境说的，而这一语境中已经明确的讨论框架，在这条新产生的笔记中就不必再重复叙述一遍了。
			* 另外，考虑到笔记内容会随着时间增长，如果我日后有了一条和「公众人物」更为相关的笔记，我也可能会修改索引笔记中的链接，使它指向这条新的笔记，而指向原来那条笔记的链接将在这条新笔记（或它之后不远处的笔记）中出现。
* <input type="checkbox" name="fchk" id="fold85"><label for="fold85">向笔记中添加新内容时，可能会发现这一内容在多个不同的语境下都可以讨论，也就是卢曼所说的「多重存储」的问题。对于这种情况，笔记之间的链接将派上用场，它负责表达这些不同位置内容之间的相互关联。</label>
	* <input type="checkbox" name="fchk" id="fold86"><label for="fold86">按 Schmidt 的说法，通过引入这样的「多重存储」，可以使得「一个话题嵌入不同的语境，启发不同领域的比较，促成了不同信息线的产生。」</label>
		*  Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
			> Conversely, embedding a topic in various contexts gives rise to different lines of information by means of opening up different realms of comparison in each case. 
	* 我并不主张使用软件的「块嵌入」功能来处理这种情况。不同语境下讨论的侧重点往往有所不同，我们所加入内容的叙述、表达方式也应该据此做出调整，而将一个语境下说出来的一句话直接放到另一个语境下，通常是会显得比较突兀的。
	* <input type="checkbox" name="fchk" id="fold90"><label for="fold90">如果同一内容的不同存放位置比较多，为这些位置的版本两两之间建立链接通常显得有些低效。此时可以采用「中心化」的策略来减少链接的总数，我们随意选取其中一个位置的版本作为「主版本」，其他版本只需要与它相互连接就足够了。</label>
		* 当然，实际中会遇到的情况也往往比较多样，有时候某两个语境下的版本之间有着更紧密的联系，这需要更为灵活的处理。
* <input type="checkbox" name="fchk" id="fold92"><label for="fold92">在我们阅读文章、制作了文献笔记以后，我们可以通过「跨语境翻译」的方式，将其中有价值的内容全部整合进由主笔记组成的系统当中，从而彻底取消不同文章、不同主题、不同学科之间的边界。</label>
	* Ahrens 在《卡片笔记写作法》中提到：「卢曼并不只是照抄他所读过的文章中的观点或引文，而是将其从一个语境转化到另一个语境」，这「很像翻译」。
	* <input type="checkbox" name="fchk" id="fold94"><label for="fold94">事实上，我的 [笔记间关联方式](../笔记间关联方式/) 和 [笔记的不同目的](../笔记的不同目的/) 两篇文章就是使用这样的方式写出来的。读者也许能在其中发现一些这样的「跨语境翻译」的痕迹。</label>
		* 值得一提的是，[笔记的不同目的](../笔记的不同目的/) 在我笔记中的样子其实稍有不同，因为我最开始只划分出了学习、知识管理和思考三类需求。
		* 当我在讨论「思考」需求的语境下，对不同人用笔记思考的方式进行了简单的汇总之后，我很快发现了一个奇怪的地方：卢曼的做法似乎和其他所有人的都不太一样。
		* 卢曼在他编号为 `9/8g` 的卡片中这样写道：「如果没能发现差异，人就无法思考。」而如果我没有以这种方式取消不同文章之间的边界，我可能永远也不会发现这里的差别。
		* 在那以后，我设想了这种差异的几种不同的解释，并最终将文章写成了各位读者现在看到的样子。
		* 当然，这两个例子其实还相对简单，因为它们的主题是已经确定的，我只需要把相关的素材汇总到这一主题下就可以了。而读者现在正在读的这篇文章则要复杂一些，我写它所用的素材散落在笔记的不同位置，它们的可组合性我是在后来才逐渐意识到的。
	* <input type="checkbox" name="fchk" id="fold100"><label for="fold100">在笔记系统建立的早期，已有的笔记内容并不多，新加入的内容可能找不到可以接纳它的语境。此时可以考虑建立一些类似于分类学的框架，使笔记系统能够容纳这些新的内容。</label>
		*  以卢曼二代卡片盒中编号由 `3` 开始的部分为例，其中许多较低层级的卡片上都只写着一些短语，而不包含完整的句子，它们并不是严格意义上的「卡片笔记」。Schmidt 给出的英文翻译如下（我就不再转译成中文了，毕竟具体内容也不那么重要）：
			```markdown
			- 3 General decision theory
				- 31 Concept of action
				- 32 Models of decision-making
				- 33 Types of decision-making model designs
					- 331 Utilitarian models
					- 332 Optimizing model
					- 333 Satisfying model (theory of acceptable decisions)
				- 34 Simplification of decision-making
					- 341 Anticipatory simplification
						- 3411 Ideology
						- 3412 Authority (organization)
						- 3413 Rules
						- 3414 Legal system
						- 3415 Unplanned structures in the field of decision-making
					- 342 Techniques of decision-making
				- 35 Organization of decision-making
			```
			*  Schmidt, Johannes. (2016). Niklas Luhmann’s Card Index: Thinking Tool, Communication Partner, Publication Machine. 10.1163/9789004325258_014. 
			* 另外，卢曼的这些卡片中还有许多指向文献笔记或永久笔记的链接（例如 [编号 `3` 的卡片](https://niklas-luhmann-archiv.de/bestand/zettelkasten/zettel/ZK_2_NB_3_1_V)）。不过从笔迹的颜色来看，这些链接应该是后来追加上去的，而最开始制作的卡片只写了上面所说的那些表示类别的短语。
	* <input type="checkbox" name="fchk" id="fold122"><label for="fold122">随着笔记数量的增长，这种情况将发生彻底的改变。能接纳新笔记的语境越来越多，「多重存储」的情况也出现得越发频繁。</label>
		*  卢曼在《与卡片盒交流》一文（[中文翻译](https://mp.weixin.qq.com/s/_aPS2ol1DxiCFX-xfl-8yg)，[英文翻译](https://luhmann.surge.sh/communicating-with-slip-boxes)）中这么写道：
			> 卡片盒需要数年时间才能达到临界水平。在此之前，它仅仅是一个容器，我们可以从中获取所放入的内容。但这种情况会随着卡片盒的规模和复杂性的增加而发生改变……卡片盒变成了一种通用工具，几乎可以容纳任何东西。
		* 到达这一阶段以后，更可能出现的情况是某条笔记有能够接纳它的语境，但却因为没能找到而误认为它不存在。这将考验我们建立、维护索引笔记与笔记间的链接网络，并利用它们高效地找到相应内容的能力。
	* <input type="checkbox" name="fchk" id="fold126"><label for="fold126">某些新内容也可能本来没有能接纳它的语境。而为了将这样的内容也整合到笔记系统中，我们需要尝试寻找讨论这一内容的全新角度，这一过程可能需要一定的创造力。</label>
		* 《与卡片盒交流》一文（[中文翻译](https://mp.weixin.qq.com/s/_aPS2ol1DxiCFX-xfl-8yg)，[英文翻译](https://luhmann.surge.sh/communicating-with-slip-boxes)）中提及，卢曼了解到「博物馆空空荡荡」，而「莫奈、毕加索或者美第奇的画展却人头攒动」。为了将这一信息整合到卡片盒中，卢曼选择了从「对时间有限的东西的偏好」的角度来探讨这个问题。
		* 这一角度不仅帮助新的内容找到了可以承接它的语境，还带来了建立新链接的可能性。
		* 在许多情况下，讨论问题的新角度也能提供在更多位置「多重存储」的可能。
	* <input type="checkbox" name="fchk" id="fold130"><label for="fold130">出现「多重存储」情况的文献笔记内容可以放入主笔记的多个不同位置中。在这一方面，我会建议将主笔记中的一个版本作为中心位置，而不是让多条笔记都引用这同一条文献笔记。</label>
		* 更具体地说，如果文献笔记中有某句话 A，它在放入主笔记的不同位置后产生了 B、C、D 这几个不同的版本。则我们可以将 B 作为存储的中心位置，它直接引用 A，并提到 C、D 是其他语境下的版本；而 C、D 都只需要直接引用 B 就可以了。
		* 原则上我们也可以主动建立由 A 指向 B 的链接，就像卢曼所做的那样。不过鉴于双链笔记软件往往有反链搜索的功能，而引用 A 的位置是唯一的（只有 B），即使我们不添加这个链接，也不会干扰我们的使用。
		* 采取这种做法的主要原因在于，位于文献笔记中的 A 存在于特定文章的语境当中，这一语境主要反映其作者的原意，不宜轻易改动，是「死」的。而主笔记 B 所在的语境则是「活」的，随着笔记的增多，其后常常会再生长出许多我们没能事先预料的内容。从这个角度来看，选取价值更高的 B 作为「中心位置」的做法更有意义。
	* <input type="checkbox" name="fchk" id="fold134"><label for="fold134">由于这种整合的依据是语境，而不是某篇文章（像原始的文献笔记那样），也不是某个特定的主题（像笔记中的多数 MOC 一样），笔记变成了几乎没有边界的「开放系统」，在这一方面具有超越传统笔记方法的强大能力。</label>
		*  卢曼在《与卡片盒交流》一文（[中文翻译](https://mp.weixin.qq.com/s/_aPS2ol1DxiCFX-xfl-8yg)，[英文翻译](https://luhmann.surge.sh/communicating-with-slip-boxes)）中提到了其卡片盒对传统「主题专业化」笔记方式的突破：
			> 要想让一个交流系统要维持更长时间，我们必须要么选择技术性很强的专业化道路，要么选择纳入随机和临时产生的信息的路线。拿笔记系统来说，我们可以选择主题专业化的方式（比如关于政府责任的笔记），也可以选择开放系统的方式。我们决定选择后者，经过26年多的成功合作（偶尔会有一些困难），我们现在可以证明这种方法的成功 —— 或者至少说这条路是可行的。
* <input type="checkbox" name="fchk" id="fold137"><label for="fold137">附录：目前的双链笔记软件并非针对这一方法设计。这会为链接建立带来一些不便，不过总体上还算是可以解决的。这里以 Logseq 为例提供一种可能的方案。</label>
	* <input type="checkbox" name="fchk" id="fold138"><label for="fold138">由于被引用的笔记往往是一句完整的话，而目前的块引用会展示被引笔记的完整内容，因此直接引用行本身的做法往往并不方便。</label>
		*  例如，假设笔记中有这样的两句话，我们希望在后一句中引用前一句：
			```markdown
			- 采取措施 A 可以达到 B 目的，但是由于机制 C 的存在，往往也会产生 D 的副作用。
			……（中间间隔的大量其他内容）
			- 针对场景 E 的处理需要考虑 A 可能引发 D 的风险，此时可考虑通过同时采取措施 F 作为补偿。
			```
		*  直接引用前面的这条笔记本身，将可能产生这样的效果，给阅读带来了不便：
			```markdown
			- 针对场景 E 的处理需要考虑((采取措施 A 可以达到 B 目的，但是由于机制 C 的存在，往往也会产生 D 的副作用。))，此时可考虑通过同时采取措施 F 作为补偿。
			```
		* 实际使用中还会遇到更复杂的情况，比如一条笔记同时引用两三条（甚至更多）其他笔记，或者某条笔记要引用一条已经引用了其他笔记的笔记，甚至还常有两条笔记相互引用对方的可能（比如说，回忆前面讨论过的多重存储问题）。
	* <input type="checkbox" name="fchk" id="fold150"><label for="fold150">此时可以采取迂回的做法，在需要被引的笔记下新起一行，其中写下这一笔记的唯一标识符（UID），引用时直接引用这个 UID 即可。</label>
		*  沿用上面的例子，现在的笔记将长成这样，看起来舒服多了。
			```markdown
			- 采取措施 A 可以达到 B 目的，但是由于机制 C 的存在，往往也会产生 D 的副作用。
				- 2302172119a
			……（中间间隔的大量其他内容）
			- 针对场景 E 的处理需要考虑((2302172115a))A 可能引发 D 的风险，此时可考虑通过同时采取措施 F 作为补偿。
			```
		* <input type="checkbox" name="fchk" id="fold158"><label for="fold158">上面的例子使用了时间戳作为某条笔记的 UID。读者也可以根据自己的喜好使用其他的 UID，比如 hash 编码等。</label>
			* 另外，我自己的习惯其实是使用 36 进制的时间戳，每隔 10 秒钟更新一次。比如，我敲下这行文字的时候，相应的时间戳是 `n2hl38`，它的简短特性为使用带来了一些便利。
			* 读者也可以为笔记想合适的标题，不过一般而言我并不推荐这一做法，见 [笔记的不同目的](../笔记的不同目的/) 关于思考工具的讨论。另外，再考虑到多重存储的问题，为这么多不同的版本都给出相应的标题也并非一件容易的事情。
		* 当我们点进这个链接的时候，Logseq 将会块聚焦到只写着 `2302172119a` 这个 UID 的行。此时点一下其上方以「面包屑」展示的上层节点的内容，就可以找到真正被引用的笔记。
	* <input type="checkbox" name="fchk" id="fold162"><label for="fold162">文献笔记整合过程中的多重存储情况也可以进行类似的处理。</label>
		*  现在文献笔记中的一行文字长成这样（这里的 UID 前加了 `L` 前缀，表示它代表文献笔记中的内容。读者也可以用自己喜欢的其他格式，比如下划线等）：
			```markdown
			- 这是文献笔记中的一句话。
				- L2302172120a
			```
		*  主笔记中的主要存储位置长成这样（读者也可以把「副本」换成其他的说法）：
			```markdown
			- 这是语境 B 中的一句话((L2302172120a))。
				- 2302172120b
				- 副本：((2302172120c))语境 C，((2302172120c))语境 D
			```
		*  而主笔记中的次要存储位置则如下所示：
			```markdown
			- 这是语境 C 中的一句话((2302172120b))。
				- 2302172120c
			```
	* <input type="checkbox" name="fchk" id="fold179"><label for="fold179">另外，建立链接的过程中，我们可能未必记得已有笔记的 UID。此时可以将各笔记的简要描述及其 UID 先写在其他位置（记事本，草稿纸，诸如此类），从而可据此建立引用。</label>
		* 不过这种不便出现的一个原因是 Logseq（至少我手上的这个版本）并不支持打开多个标签页，同时查看几条不同的笔记。否则的话，我们直接照着另一个标签页里所看到的 UID 抄上去就可以了。（如果有读者了解相关的信息，比如已实现的软件、插件等，也欢迎在评论区告诉我。）
		* 其实我个人由于使用习惯、历史遗留问题等多个方面的原因，并不使用常见的双链笔记软件，而是在 Vim 里自己加了一些简单的小功能，用来实现链接跳转、反链搜索等。这使得我的 UID 可以和笔记的本体放在同一行里，并且沿链接跳转也是默认打开新的标签页。如果可能的话，希望有更多人在用的双链笔记软件也能不断地改进，满足不同用户的期待吧。

