//https://www.techiedelight.com/implement-select-all-check-box-html-javascript/
function expandFoldAll(){  
	this.checked = ~this.checked;
	var ele=document.getElementsByName('fchk');  
	//document.querySelectorAll('input[type="checkbox"]');
	for(var chk of ele){  
		if(chk.type=='checkbox')  
			chk.checked=this.checked;  
	}  
}  
