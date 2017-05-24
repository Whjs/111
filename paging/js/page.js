jQuery.fn.extend({
	"initPage": function(pageMessage){
		var _this = this;
		var page = {
			sumPage: pageMessage.sumPage || 7,
			showPage: pageMessage.showPage || 7,
			textPage:  pageMessage.textPage|| '下一页',
			prevPage: pageMessage.prevPage || '上一页',
			startAndEndPage: pageMessage.startAndEndPage ? true : false,
			callback: pageMessage.callback || pageCallback,
			nowPage: 1
		}
		function pageCallback(){}
		// 初始化
		pageListInit();
		pageListClick();
		//事件绑定
		function pageListClick(){
			$(_this).find('ul li').each(function(index) {
				$(this).unbind('click');
				$(this).bind('click', function(){
					var pageData = $(this).attr('page-data');
					var oldPage = parseInt($(_this).find('ul li[class*="j-page-option"]').attr('page-data'));
					pageListChange(oldPage, pageData);
				})
			});
		}
		//当页码改变是触发的函数
		function pageListChange(index, pageData){
			var n = 0, 
				listStr = '',
				centerNumber = Math.ceil(page.showPage/2);
			switch (pageData) {
				case 'startPage':
					n = 1;
					break;
				case 'endPage':
					n = page.sumPage;
					break;
				case 'prevPage':
					index > 1 ? n = index - 1 : n = 1;
					break;
				case 'textPage':
					index < page.sumPage ? n = index + 1 : n = page.sumPage;
					break;
				case 'omit':
					return;
					break;
				default:
					n = parseInt(pageData);
					break;
			}
			if( n ===1 ){
				listStr = page.startAndEndPage ? '<ul class="j-page-list">'+
			'<li class="j-page-parv j-page-forbid" page-data="startPage">首页</li>'+
			'<li class="j-page-parv j-page-forbid" page-data="prevPage">'+ page.prevPage +'</li>' : '<ul class="j-page-list" page-data="prevPage">'+
			'<li class="j-page-parv j-page-forbid" page-data="prevPage">'+ page.prevPage +'</li>';
			}else{
				listStr = page.startAndEndPage ? '<ul class="j-page-list">'+
			'<li class="j-page-parv" page-data="startPage">首页</li>'+
			'<li class="j-page-parv" page-data="prevPage">'+ page.prevPage +'</li>' : '<ul class="j-page-list" page-data="prevPage">'+
			'<li class="j-page-parv" page-data="prevPage">'+ page.prevPage +'</li>';
			}
			if(page.sumPage > page.showPage){
				if( n < page.showPage - 2){
					for(var i = 1; i < page.showPage + 1; i++){
						switch(i){
							case n : listStr += '<li class="j-page-option" page-data='+i+'>'+i+'</li>'; break;
							case page.showPage - 1: listStr += '<li class="j-page-omit" page-data="omit">...</li>'; break;
							case page.showPage: listStr += '<li page-data='+ page.sumPage +'>'+ page.sumPage +'</li>'; break;
							default: listStr += '<li page-data='+i+'>'+i+'</li>'
						}
					}
				}else if( n > page.showPage - 3 && n < page.sumPage - page.showPage + 3 ){
					for(var i = 1; i < page.showPage + 1; i++){
						switch(i){
							case 1: listStr += '<li page-data='+i+'>'+i+'</li>'; break;
							case 2: listStr += '<li class="j-page-omit" page-data="omit">...</li>'; break;
							case centerNumber: listStr += '<li class="j-page-option" page-data='+n+'>'+n+'</li>'; break;
							case page.showPage - 1: listStr += '<li class="j-page-omit" page-data="omit">...</li>'; break;
							case page.showPage: listStr += '<li page-data='+ page.sumPage +'>'+ page.sumPage +'</li>'; break;
							default: listStr += '<li page-data='+ (n + i - centerNumber) +'>'+ (n + i - centerNumber) +'</li>';
						}
					}
				}else{
					for(var i = 1; i < page.showPage + 1; i++){
						switch(i){
							case 1: listStr += '<li page-data='+i+'>'+i+'</li>'; break;
							case 2: listStr += '<li class="j-page-omit" page-data="omit">...</li>'; break;
							case n - page.sumPage +  page.showPage: listStr += '<li class="j-page-option" page-data='+n+'>'+n+'</li>'; break;
							case page.showPage: listStr += '<li page-data='+ page.sumPage +'>'+ page.sumPage +'</li>'; break;
							default: listStr += '<li page-data='+ (page.sumPage - page.showPage + i) +'>'+ (page.sumPage - page.showPage + i) +'</li>';
						}
					}
				}
				listStr += endShowPage(n);
			}else{
				for(var i = 1; i < page.sumPage + 1; i++){
					i === n ? listStr += '<li class="j-page-option" page-data='+i+'>'+i+'</li>' : listStr += '<li page-data='+i+'>'+i+'</li>'
				}
				listStr += endShowPage(n);
			}
			$(_this).html(listStr);
			pageListClick();
			page.callback(n);
		}
		//页码变化时 最后一部分页码 包括下一页这些，因代码重复所以抽出
		function endShowPage(n){
			var listStr='';
			if(page.sumPage === n){
				listStr += page.startAndEndPage ? '<li class="j-page-parv j-page-forbid" page-data="textPage">'+ page.textPage +'</li><li class="j-page-parv j-page-forbid" page-data="endPage">尾页</li></ul>' : '<li class="j-page-parv j-page-forbid" page-data="textPage">'+ page.textPage +'</li></ul>';
			}else{
				listStr += page.startAndEndPage ? '<li class="j-page-parv" page-data="textPage">'+ page.textPage +'</li><li class="j-page-parv" page-data="endPage">尾页</li></ul>' : '<li class="j-page-parv" page-data="textPage">'+ page.textPage +'</li></ul>';
			}
			return listStr;
		}
		//初始化页码函数
		function pageListInit(){
			var listStr = page.startAndEndPage ? '<ul class="j-page-list"><li class="j-page-parv j-page-forbid" page-data="startPage">首页</li><li class="j-page-parv  j-page-forbid" page-data="prevPage">'+ page.prevPage +'</li>' : '<ul class="j-page-list" page-data="prevPage"><li class="j-page-parv j-page-forbid" page-data="prevPage">'+ page.prevPage +'</li>';
			if(page.sumPage > page.showPage){
				for(var i = 1; i < page.showPage + 1; i++){
					switch(i){
						case 1 : listStr += '<li class="j-page-option" page-data='+i+'>'+i+'</li>'; break;
						case page.showPage - 1: listStr += '<li class="j-page-omit" page-data="omit">...</li>'; break;
						case page.showPage: listStr += '<li page-data='+ page.sumPage +'>'+ page.sumPage +'</li>'; break;
						default: listStr += '<li page-data='+i+'>'+i+'</li>'
					}
				}
				listStr += page.startAndEndPage ? '<li class="j-page-parv" page-data="textPage">'+ page.textPage +'</li><li class="j-page-parv" page-data="endPage">尾页</li></ul>' : '<li class="j-page-parv" page-data="textPage">'+ page.textPage +'</li></ul>';
			}else{
				for(var i = 1; i < page.sumPage + 1; i++){
					i === 1 ? listStr += '<li class="j-page-option" page-data='+i+'>'+i+'</li>' : listStr += '<li page-data='+i+'>'+i+'</li>'
				}
				listStr += page.startAndEndPage ? '<li class="j-page-parv" page-data="textPage">'+ page.textPage +'</li><li class="j-page-parv" page-data="endPage">尾页</li></ul>' : '<li class="j-page-parv" page-data="textPage">'+ page.textPage +'</li></ul>';
			}
			$(_this).html(listStr);
			page.callback(1);
		}
	}
})