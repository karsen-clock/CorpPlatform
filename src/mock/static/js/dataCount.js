//绑定事件触发查询提交按钮
function getDataCount(){
document.getElementById("getDataCountForm").submit();
};
//jqeury setup
$.ajaxSetup({
  dataType: "json",  
  beforeSend: function(xhr, settings){  
      var csrftoken = $.cookie('csrftoken');  
      xhr.setRequestHeader("X-CSRFToken", csrftoken);  
  },
});
//编辑页ajax请求
	function getDataCountAjax(startDate,endDate) {
		$.ajax({
			type : 'post',
			url : '/getDataCount',
			data : {
				"StartDate":startDate,
				"EndDate":endDate,
				"BuId":82
			},
			cache : false,
			dataType : 'json',
			success:function(data){
				getTestCasesCountDatSource(data.categories,data.casesCount);
				getTestResponseTimeDatSource(data.categories,data.time);
				getSuccessRateDatSource(data.categories,data.rate);
				getSuccessRateBuildNoDatSource(data.successRateBuildNo);
}
});
}

//http://ws.logging.ctripcorp.com/exceptions/exception-list?fromDate=2015-12-09%2014:41:00&toDate=2015-12-30%2015:41:00&buId=82
//http://ws.logging.ctripcorp.com/loglevel/host-list/480112?fromDate=2015-11-25%2015:03:00&toDate=2015-12-30%2016:03:00&logLevels=3,4
//http://ws.logging.ctripcorp.com/loglevel/timeline/app/{0}?fromDate={0}&toDate={1}&logLevels=3,4 