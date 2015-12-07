//绑定事件触发查询提交按钮
function getInterfaceList(){
document.getElementById("getInterfaceForm").submit();
};
//增加MOCK接口绑定button事件
function addInterface(){
document.getElementById("addMockForm").submit();
};
//增加MOCK接口绑定启动服务事件
function runservice(){
document.getElementById("runServiceForm").submit();
};

//删除确认框提示
function getTableDelete(currentTd){
	var currentTr = currentTd.parentNode.parentNode.parentNode; 
	protocol=currentTr.cells[0].innerHTML;
	interfaceName=currentTr.cells[1].innerHTML;
	businessName=currentTr.cells[2].innerHTML;
	configParameter=currentTr.cells[3].innerHTML;
	isValid=currentTr.cells[7].innerHTML;
	$(function() {
       $("#DeleteModal").modal("hide");
       $("#DeleteModal").modal("show");
       $('#deleteConfimrm').click(function(){
	   deleteSelectedInterface(protocol,interfaceName);
	   })
})
}
//编辑确认框提示
function getTableEdit(currentTd){
	var currentTr = currentTd.parentNode.parentNode.parentNode; 
	protocol=currentTr.cells[0].innerHTML;
	interfaceName=currentTr.cells[1].innerHTML;
	businessName=currentTr.cells[2].innerHTML;
	configParameter=currentTr.cells[3].innerHTML;
	isValid=currentTr.cells[7].innerHTML;
	$(function() {
       $("#EditModal").modal("hide");
       $("#EditModal").modal("show");
       document.getElementById("protocolModal").value=protocol
       document.getElementById("interfaceNameModal").value=interfaceName
       document.getElementById("businessNameModal").value=businessName
       document.getElementById("mockConfigModal").value=configParameter
       $("#EditModalConfirm").click(function(){
       businessNameEdited=document.getElementById("businessNameModal").value
       configParameterEdited=document.getElementById("mockConfigModal").value
		editSelectedInterface(protocol,interfaceName,businessNameEdited,configParameterEdited)
	   })
})
}


//jqeury setup
$.ajaxSetup({
  dataType: "json",  
  beforeSend: function(xhr, settings){  
      var csrftoken = $.cookie('csrftoken');  
      xhr.setRequestHeader("X-CSRFToken", csrftoken);  
  },
});

//删除发送ajax请求
	function deleteSelectedInterface(protocol, interfaceName) {
		$.ajax({
			type : 'post',
			url : '/deleteInterfaceConfig',
			data : {
				"protocol" : protocol,
				"interfaceName" : interfaceName
			},
			cache : false,
			dataType : 'json',
			success:function(data){
			Confirm.show('Message', data.message);
			getInterfaceList();
}
});
}

//编辑页ajax请求
	function editSelectedInterface(protocol,interfaceName, businessName,configParameter) {
		$.ajax({
			type : 'post',
			url : '/editInterfaceConfig',
			data : {
				"protocol":protocol,
				"interfaceName":interfaceName,
				"businessName":businessName,
				"configParameter":configParameter
			},
			cache : false,
			dataType : 'json',
			success:function(data){
			Confirm.show('Message', data.message);
			getInterfaceList();
}
});
}

//bootstrap样式js
