## <center>Vim-go操作笔记</center>
### Hello World
`vi main.go`

### Run it
- **运行当前文件：** `:GoRun %` 后台调用 `go run`
- **运行整个包：** `:GoRun`

### Build it
- **编译：** `:GoBuild` 后台调用 `:go build` ，而且更聪明
- 不会生成二进制文件，可以多次调用 `:GoBuild` ，不会污染工作目录
- 自动进入源程序包的目录
- 解析所有错误，并在快速修复列表（quickfix list）中显示
- It automatically detects the GOPATH and modifies it if needed (detects projects such as gb, Godeps, etc..)
- Runs async if used within Vim 8.0.xxx or NeoVim

### Fix it
- **在错误中跳转：** `:cnext`、`:cprevious`
- 修复错误，保存编译，quickfix window 会自动关闭
- `:set autowrite` 不用手动保存，加快迭代速度
- `:GoBuild` 会自动跳转到第一个错误，不想跳转 `:GoBuild!`
- In all the `go` commands, such as `:GoRun`, `:GoInstall`, `:GoTest`, etc.., whenever there is an error the quickfix window always will pop up.
- Vimrc 配置：
	```vimrc
	set autowrite
	map <C-n> :cnext<CR>
	map <C-m> :cprevious<CR>
	nnoremap <leader>a :cclose<CR>
	```
- Vim 有两种错误列表，一种是位置列表（location list）另一种是快速修复列表。
- **位置列表跳转：** `lnext`、`lprevious`
- Vim-go中某些命令会打开一个位置列表，因为位置列表与一个窗口相关联，并且每个窗口可以有一个单独的列表。这意味着，可以有多个窗口和多个位置列表，一个用于构建，一个用于检查，一个用于测试，等等。
- Some people prefer to use only `quickfix` though. If you add the following to your `vimrc` all lists will be of type `quickfix`:
	```vimrc
	" 所有列表使用 quickfix
	let g:go_list_type = "quickfix"
	```

### Test it
- **测试：** `:GoTest` 后台调用 `go test`，并且有像 `:GoBuild` 一样的改进。如果有任何测试错误，则会再次打开快速修复列表。
- 另一个改进是，不必打开测试文件本身，比如在主程序调用 `GoTest` 也能达到相同目的。
- `:GoTest` times out after 10 seconds by default. This is useful because Vim is not async by default. You can change the timeout value with
	```vimrc
	let g:go_test_timeout = '10s'
	```
- **另两个简化测试文件的命令：**
	+ 第一个：`:GoTestFunc` This only tests the function under your cursor. 进入到某些函数测试，这对于只想对某些函数测试很有用。
	+ 第二个：`:GoTestCompile` 测试不仅需要成功通过，而且必须毫无问题地进行编译。`:GoTestCompile` 像`:GoBuild` 一样编译测试文件，并在出现任何错误时打开一个快速修复程序，但是，这不会运行测试。如果要进行大量的大型测试，这将非常有用。
- As with `:GoBuild` we can add a mapping to easily call `:GoTest` with a key combination. Add the following to your `.vimrc`:
	```vimrc
	autocmd FileType go nmap <leader>t  <Plug>(go-test)
	```
- Let's make building Go files simpler. First, remove the following mapping we added previously:
```vimrc
autocmd FileType go nmap <leader>b  <Plug>(go-build)
```
- 我们将添加一个改进的映射。为了使它对任何Go文件都是无缝的，我们可以创建一个简单的Vim函数来检查Go文件的类型，并执行`:GoBuild` 或`:GoTestCompile`。
```vimrc
" run :GoBuild or :GoTestCompile based on the go file
function! s:build_go_files()
  let l:file = expand('%')
  if l:file =~# '^\f\+_test\.go$'
    call go#test#Test(0, 1)
  elseif l:file =~# '^\f\+\.go$'
    call go#cmd#Build(0)
  endif
endfunction

autocmd FileType go nmap <leader>b :<C-u>call <SID>build_go_files()<CR>
```

### Cover it
- 让我们进一步深入测试的世界。(Let's dive further into the world of tests.) 测试真的很重要。Go具有显示源代码覆盖范围的绝佳方法。使用vim-go可以轻松查看代码覆盖范围，而不会以非常优雅的方式离开Vim。Vim-go makes it easy to see the code coverage without leaving Vim in a very elegant way.
- `:GoCoverage` 后台调用 `test -coverprofile tempfile` 它解析配置文件中的行，然后动态更改源代码的语法以反映覆盖范围。对哪个函数进行测试，哪个函数块就以绿色显示。
- **清除语法突出：** `:GoCoverageClear`
- 因为 `:GoCoverage` & `:GoCoverageClear` 一起使用很频繁，使用 `:GoCoverageToggle` 可以简化调用和清除的过程。
- 如果不喜欢 vim-go 的内部视图，可以调用 `:GoCoverageBrowser` 后台调用 `go tool cover` 创建HTML页面，然后再默认浏览器打开。(和作者谈谈是否可以远程)
- **注意：** `:GoCoverageXXX` 命令不会创建任何类型的临时文件，也不会污染工作流程。
- Vimrc配置：
	```vimrc
	autocmd FileType go nmap <Leader>c <Plug>(go-coverage-toggle)
	```

### Edit it
#### Imports
- 保存自动格式化，默认开启，`let g:go_fmt_autosave = 0` 可以禁用。
- **格式化：** `:GoFmt` 后台调用 `gofmt`
- 以大写形式打印 `gopher` 使用 `strings` 包：
	```go
	fmt.Println(strings.ToUpper("gopher"))
	```
- **导包：** `:GoImport`，例如：`:GoImport strings`，支持补全，比如：`:GoImport s`
- **编辑导入路径：** `GoImportAs` 和 `GoDrop`，`GoImportAs` 和 `GoImport` 相同，但是它允许更改程序包名称。例如 `:GoImportAs str strings` 把 strings 导入并取别名为 str。`:GoDrop strings` 从声明中移除 strings 包。
- `goimports` 是 `gofmt` 的替代品，并且更好。
- 有两种使用方式：
	+ First(recommended)：告诉 vim-go 保存文件时使用。每当保存文件时 `goimports` 都会自动格式化并重写导入声明（import declarations）。
		```vimrc
		let g:go_fmt_command = "goimports"
		```
	+ Second：有些人不喜欢使用 `goimports` 因为在大型代码库上它可能很慢。在这种情况下，我们还有 `:GoImports` 命令，用来显式调用 `goimports`。

#### Text objects
- Let us show more editing tips/tricks. There are two text objects that we can use to change functions. Those are `if` and `af`. `if` means inner function and it allows you to select the content of a function enclosure. (表示内部功能，它允许选择功能柜的内容。)
- Put your cursor on the `func` keyword. Now execute `dif` in *normal mode* and You'll see that function body is removed. The great thing is that your cursor can be anywhere starting from the `func` keyword until the closing right brace `}`.
- 作者为 vim-go 明确写了像这样的动作，它具有 Go AST 意识，因此它的功能非常出色。(It's Go AST aware and thus its capabilities are really good.)
- Previously we were using regexp-based text objects, which leads to problems. (以前，使用正则表达式的文本对象，会导致问题) For example in this example, put your cusor to the anonymous functions' `func` keyword and execute `dif` in *normal mode.* You'll see that only the body of the anonymous function is delete. (把光标放在 `func` 上，在正常模式使用 `dif`，仅匿名函数主体被删除。)
- We have only used the `d` operator (delete) so far. However it's up to you. For example you can select it via `vif` or yank(copy) with `yif`. (目前只用了删除的文本对象，可试一下其它的。)
- `af` 表示功能。该文本对象包括整个函数声明。(We also have `af`, which means `a function`. This text object includes the whole function declaration.)
- So here is the great thing. (所以这是伟大的事情) Because of `motion` we have full knowledge about every single syntax node. (由于动作，对语法节点都有全面的了解) Put your cursor on top of the `func` keyword or anywhere below or above (doesn't matter). If you now execute `vaf`, you'll see that the function declaration is being selected, along with the doc comment as well! You can for example delete the whole function with `daf`, and you'll see that the comment is gone as well. (光标放在func上下方，执行 vaf 会选择函数声明和 doc 注释，使用 daf 删除整个函数以及注释) Go ahead and put your cursor on top of the comment and execute `vif` and then `vaf`. You'll see that it selects the function body, even though your cursor is outside the function, or it selects the function comments as well. (将光标置于注释顶部，先 vif 再 vaf，它选择了函数主体，即使光标在函数外部，也选择了函数注释)
- This is really powerful and this all is thanks to the knowledge we hava from the motion. If you don't like comments being a part of the function declaration, you can easily disable it.
	```vimrc
	" 1 启用， 0 禁用。
	let g:go_textobj_include_function_doc = 1
	```

#### Struct split and join
- There is a great plugin that allows you to split or join Go structs. It's actually not a Go plugin, but it has support for Go structs.
	```vimrc
	Plug 'AndrewRadev/splitjoin.vim'
	```
- Once you have installed the plugin, change the main.go file to: (安装插件后，将 main.go 文件更改为)
- Put your cursor on the same line as the struct expression. Now type `gS`. This will split the struct expression into multiple lines. And you can even reverse it. If your cursor is still on the foo variable, execute `gJ` in *normal mode*. You'll see that the field definitions are all joined. (将光标与 struct 表达式放在同一行。现在输入 gS 会将结构表达式分成多行，也可以逆转，将光标放在 foo 变量上，执行 gJ 所有字段会加入) This doesn't use any AST-aware tools, so for example if you type `gJ` on top of the fields, you'll see that only two fields are joined. (它不使用任何支持 AST 的工具，因此，例如，如果您在字段上方键入 gJ，则会看到仅两个字段连接在一起)

#### Snippets
- Vim-go supports two popular plugins. Ultisnips and neosnippet. (支持两个流行的代码片段插件) By default, if you have `Ultisnips` installed it'll work.
	```vimrc
	Plug 'SirVer/ultisnips'
	```

#### vimrc improvements
- When you save your file, `gofmt` shows any errors during parsing the file. If there are any parse errors it'll show them inside a quickfix list. This is enabled by default. Some people don't like it. (保存，gofmt 会在解析文件时显示任何错误，如果有任何解析错误会在快速修复列表中显示) To disable it add:
	```vimrc
	let g:go_fmt_fail_silently = 1
	```
- You can change which case it should apply while converting. (更改转换时应用的情况) By default vim-go uses `snake_case`. But you can also use `CamelCase` if you wish. For example if you wish to change the default value to camel case use the following setting: (默认使用下划线风格，可以根据需要更改为驼峰式风格)
	```vimrc
	let g:go_addtags_transform = "camelcase"
	```

### Beautify it
- By default we only have a limited syntax highlighting enabled. There are two main reasons. (默认仅启用有限的语法突出显示功能，有两个主要原因) First is that people don't like too much color because it causes too much distraction. (太多颜色引起干扰) The second reason is that it impacts the performance of Vim a lot. (对vim的性能影响很大) We need to enable it explicitly.
	```vimrc
	let g:go_highlight_types = 1
	let g:go_highlight_fields = 1
	let g:go_highlight_functions = 1
	let g:go_highlight_function_calls = 1
	let g:go_highlight_operators = 1
	let g:go_highlight_extra_types = 1
	let g:go_highlight_build_constraints = 1
	let g:go_highlight_generate_tags = 1
	```
- We have a lot more highlight settings, these are just a sneak peek of it. For more check out the settings via `:help go-settings`

#### vimrc improvements
- Some people don't like how the tabs are shown. By default Vim shows `8` spaces for a single tab. However it's up to us how to represent in Vim. The following will change it to show a single tab as 4 spaces:
	```vimrc
	autocmd BufNewFile,BufRead *.go setlocal noexpandtab tabstop=4 shiftwidth=4
	" colorscheme
	Plug 'fatih/molokai'
	"enable molokai with original color scheme and 256 color version
	let g:rehash256 = 1
	let g:molokai_original = 1
	colorscheme molokai
	```

