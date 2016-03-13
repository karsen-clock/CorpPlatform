function showConfigParmaeter(ConfigTemplate){
	var t=document.getElementById("ConfigParameter");
	if(ConfigTemplate=="SOA1.0")
		{
			var res=[{
	"request": {
		"uri": "/flight-product-searchws/flightsearch.asmx",
		"xpaths": {
			"/request/parameters/id/text()": "1"
		}
	},
	"response": {
		"headers": {
			"Content-Type": "text/xml;charset=utf-8"
		},
		"file": {
			"charset": "utf-8",
			"name": "fligtsearch.response"
		}
	}
}];
		t.value=JSON.stringify(res, null, 4); 
		}
	else if(ConfigTemplate=="Proxy-Default")
		{
			var res=[{
					"request": {
						"uri": "/flight-product-searchws/flightsearch.asmx"
					},
					"response": {
						"proxy": "http://fltws.fws.qa.nt.ctripcorp.com/flight-product-searchws/flightsearch.asmx"
					}
				}];		
			t.value=JSON.stringify(res, null, 4); 
		}
	else if(ConfigTemplate=="SOA2.0")
	{
		var res=[{
				"description": "这里的response也可以参照SOA1.0指定文件内容响应",
				"request": {
					"uri": "/json_response_shortcut"
				},
				"response": {
					"json": {
						"foo": "foo"
					}
				}
			}];		
		t.value=JSON.stringify(res, null, 4); 
	}
	else if(ConfigTemplate=="Form")
	{
		var res=[{
				"request": {
					"method": "post",
					"forms": {
						"name": "dreamhead"
					}
				},
				"response": {
					"text": "foobar"
				}
			}];
		t.value=JSON.stringify(res, null, 4); 
	}
	else if(ConfigTemplate=="Redirect")
	{
		var res=[{
				"request": {
					"uri": "/redirect"
				},
				"redirectTo": "http://www.baidu.com"
			}];
		t.value=JSON.stringify(res, null, 4); 
	}
	else if(ConfigTemplate=="Asynchronous")
	{
		var res=[{
				"request": {
					"uri": "/event"
				},
				"response": {
					"text": "post_foo"
				},
				"on": {
					"complete": {
						"async": "true",
						"latency": 500,
						"post": {
							"url": "http://www.2345.com/target",
							"content": "content"
						}
					}
				}
			}];
		t.value=JSON.stringify(res, null, 4); 
	}
	else
	{
		var res=[{
				"request": {
					"uri": {
						"match": "/proxy/.*"
					}
				},
				"response": {
					"latency": {
						"duration": 1,
						"unit": "second"
					}
				}
			}];
	
	}
	$('#result').html(syntaxHighlight(t.value));
};

//触发执行代码高亮，分别在页面初始化以及鼠标移出文本框进行
function highLightCode(){
		var configDefault=document.getElementById("ConfigParameter").value;
			JSON.stringify(configDefault, null, 4);
			$('#result').html(syntaxHighlight(configDefault));
	}
//代码高亮显示
function syntaxHighlight(json) {
    if (typeof json != 'string') {
        json = JSON.stringify(json, undefined, 2);
    }
    json = json.replace(/&/g, '&').replace(/</g, '<').replace(/>/g, '>');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function(match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}