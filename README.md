* 本博客下的文章可在 [GitHub Pages](https://functoreality.github.io/blog-pkm/) 下查看。
* 文章存放于 `contents/` 的各子目录下，对应的 `raw.md` 为由人维护的 Markdown 源文件，`index.md` 由脚本自动生成，是供读者查看的最终文档。
	* 每篇文章都使用一个专门的目录存放，从而与文中用到的图片位于同一目录下，不同文章的图片不易混淆。
	* 读者能够折叠和展开文章中的部分内容。这一功能的实现需要 `assets/main.scss`，以及在生成的各个 `index.md` 文件中加上特定的 HTML 标记。这部分工作由脚本自动完成。
	* 运行 Python3 程序 `formatter.py` 将会遍历 `contents/` 下的各子文件夹，生成供读者查看的最终文件 `index.md`。

license: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
