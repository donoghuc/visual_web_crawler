
(function() {
  var fn = function() {
    Bokeh.safely(function() {
      (function(root) {
        function embed_document(root) {
          
        var docs_json = '{"94bdca91-0cfe-4e2e-9186-020b0d9e9f2d":{"roots":{"references":[{"attributes":{},"id":"d7ee4ecb-505b-411c-a6fd-46bac1219dec","type":"ResetTool"},{"attributes":{"source":{"id":"c988a591-6c43-4124-8868-8dd7d87a4ed5","type":"ColumnDataSource"}},"id":"1f43b28c-4599-4487-ac38-f63d65730dfd","type":"CDSView"},{"attributes":{"callback":null},"id":"ddd2a5b2-bbae-4396-a8eb-2610553a8213","type":"DataRange1d"},{"attributes":{"dimension":1,"grid_line_color":{"value":null},"plot":{"id":"23ca301c-d79c-43a3-ba8b-62f117fd7e30","subtype":"Figure","type":"Plot"},"ticker":{"id":"cefea559-1c84-44e2-b196-7501819acbd0","type":"BasicTicker"}},"id":"b66387f2-cca0-443f-88d6-8967b7fdfdaa","type":"Grid"},{"attributes":{},"id":"d8bb8563-f593-4237-8310-1aaf6fbd7932","type":"BasicTickFormatter"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"xs":{"field":"xs"},"ys":{"field":"ys"}},"id":"e47712dc-bf22-42d6-a0a2-e2d03ccc5d7e","type":"MultiLine"},{"attributes":{},"id":"2c42a435-b173-413f-a0b3-968c0316b7cc","type":"SaveTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"c364622e-5065-47f5-9b79-92a9786bbf07","type":"BoxAnnotation"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"a9e162e2-d40d-4c2d-9979-048e26b4c819","type":"PanTool"},{"id":"3c457735-9baf-4daf-abea-ac855180910f","type":"WheelZoomTool"},{"id":"a7255a00-1ca2-454d-b676-878904c0e140","type":"BoxZoomTool"},{"id":"2c42a435-b173-413f-a0b3-968c0316b7cc","type":"SaveTool"},{"id":"d7ee4ecb-505b-411c-a6fd-46bac1219dec","type":"ResetTool"},{"id":"f125d9ee-761b-4de1-8436-640591a867d8","type":"HelpTool"},{"id":"87bc545c-bb6a-472a-9148-9a0b7e787286","type":"HoverTool"}]},"id":"54438453-9b99-4e11-950a-fec347a205b1","type":"Toolbar"},{"attributes":{},"id":"bb1c0d5e-e3f2-4bbd-aac1-748689026bdb","type":"LinearScale"},{"attributes":{"formatter":{"id":"d8bb8563-f593-4237-8310-1aaf6fbd7932","type":"BasicTickFormatter"},"plot":{"id":"23ca301c-d79c-43a3-ba8b-62f117fd7e30","subtype":"Figure","type":"Plot"},"ticker":{"id":"cefea559-1c84-44e2-b196-7501819acbd0","type":"BasicTicker"},"visible":false},"id":"06657cee-0173-4691-ad39-386d3b1b4b13","type":"LinearAxis"},{"attributes":{},"id":"a9e162e2-d40d-4c2d-9979-048e26b4c819","type":"PanTool"},{"attributes":{"data_source":{"id":"dc1cee8d-890a-4ad1-8b70-4789a561b611","type":"ColumnDataSource"},"glyph":{"id":"63a4a290-325b-4d23-93d8-d6aa5b95e675","type":"MultiLine"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"e47712dc-bf22-42d6-a0a2-e2d03ccc5d7e","type":"MultiLine"},"selection_glyph":null,"view":{"id":"0b8c2c5d-1f5d-4c0d-995d-0eaefa6c15ba","type":"CDSView"}},"id":"81be4956-44e4-4310-b6bd-f5c76edefbc1","type":"GlyphRenderer"},{"attributes":{"background_fill_alpha":{"value":0.5},"background_fill_color":{"value":"black"},"below":[{"id":"a841b1e1-2c32-4839-98e6-e204ecc98ebd","type":"LinearAxis"}],"border_fill_alpha":{"value":0.5},"border_fill_color":{"value":"whitesmoke"},"left":[{"id":"06657cee-0173-4691-ad39-386d3b1b4b13","type":"LinearAxis"}],"renderers":[{"id":"a841b1e1-2c32-4839-98e6-e204ecc98ebd","type":"LinearAxis"},{"id":"db8d9cb9-4129-417a-b41e-33662896894a","type":"Grid"},{"id":"06657cee-0173-4691-ad39-386d3b1b4b13","type":"LinearAxis"},{"id":"b66387f2-cca0-443f-88d6-8967b7fdfdaa","type":"Grid"},{"id":"c364622e-5065-47f5-9b79-92a9786bbf07","type":"BoxAnnotation"},{"id":"81be4956-44e4-4310-b6bd-f5c76edefbc1","type":"GlyphRenderer"},{"id":"3c1ffb09-2843-4988-bfb5-0b47f4239469","type":"GlyphRenderer"}],"sizing_mode":"scale_both","title":{"id":"432f38af-31bd-4e71-adec-56abc1403948","type":"Title"},"toolbar":{"id":"54438453-9b99-4e11-950a-fec347a205b1","type":"Toolbar"},"toolbar_location":"above","x_range":{"id":"401ea83b-3c82-4d70-b926-e77c2210fc49","type":"DataRange1d"},"x_scale":{"id":"13626551-14de-4887-b485-e16973dd14e0","type":"LinearScale"},"y_range":{"id":"ddd2a5b2-bbae-4396-a8eb-2610553a8213","type":"DataRange1d"},"y_scale":{"id":"bb1c0d5e-e3f2-4bbd-aac1-748689026bdb","type":"LinearScale"}},"id":"23ca301c-d79c-43a3-ba8b-62f117fd7e30","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"c988a591-6c43-4124-8868-8dd7d87a4ed5","type":"ColumnDataSource"},"glyph":{"id":"fad0abe8-a5d6-48f3-a419-816f3923cd57","type":"Circle"},"hover_glyph":null,"muted_glyph":null,"name":"nodes","nonselection_glyph":{"id":"8b5d5ae3-d8e4-45ae-b786-0a5d72593c4e","type":"Circle"},"selection_glyph":null,"view":{"id":"1f43b28c-4599-4487-ac38-f63d65730dfd","type":"CDSView"}},"id":"3c1ffb09-2843-4988-bfb5-0b47f4239469","type":"GlyphRenderer"},{"attributes":{"callback":null,"column_names":["node_x","node_y","desc","colors"],"data":{"colors":["cyan","blue","red","yellow","green","purple","grey","pink","black","white","brown"],"desc":["http://localhost:6543/demo/node0","http://localhost:6543/demo/node1","http://localhost:6543/demo/node2","http://localhost:6543/demo/node3","http://localhost:6543/demo/node4","http://localhost:6543/demo/node5","http://localhost:6543/demo/node6","http://localhost:6543/demo/node7","http://localhost:6543/demo/node8","http://localhost:6543/demo/node9","http://localhost:6543/demo/node10"],"node_x":[0,-1,0,1,-1,0,1,-1,0,1,0],"node_y":[0,-1,-1,-1,-2,-2,-2,-3,-3,-3,-4]}},"id":"c988a591-6c43-4124-8868-8dd7d87a4ed5","type":"ColumnDataSource"},{"attributes":{},"id":"571e954b-7cea-44e9-a369-ed9be4b03922","type":"BasicTickFormatter"},{"attributes":{},"id":"3c457735-9baf-4daf-abea-ac855180910f","type":"WheelZoomTool"},{"attributes":{"callback":null},"id":"401ea83b-3c82-4d70-b926-e77c2210fc49","type":"DataRange1d"},{"attributes":{"callback":null,"names":["nodes"],"tooltips":[["URL","@desc"]]},"id":"87bc545c-bb6a-472a-9148-9a0b7e787286","type":"HoverTool"},{"attributes":{},"id":"13626551-14de-4887-b485-e16973dd14e0","type":"LinearScale"},{"attributes":{"line_color":{"field":"line_color"},"xs":{"field":"xs"},"ys":{"field":"ys"}},"id":"63a4a290-325b-4d23-93d8-d6aa5b95e675","type":"MultiLine"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":20},"x":{"field":"node_x"},"y":{"field":"node_y"}},"id":"8b5d5ae3-d8e4-45ae-b786-0a5d72593c4e","type":"Circle"},{"attributes":{"source":{"id":"dc1cee8d-890a-4ad1-8b70-4789a561b611","type":"ColumnDataSource"}},"id":"0b8c2c5d-1f5d-4c0d-995d-0eaefa6c15ba","type":"CDSView"},{"attributes":{"fill_color":{"field":"colors"},"line_color":{"value":"#1f77b4"},"size":{"units":"screen","value":20},"x":{"field":"node_x"},"y":{"field":"node_y"}},"id":"fad0abe8-a5d6-48f3-a419-816f3923cd57","type":"Circle"},{"attributes":{"callback":null,"column_names":["xs","ys","line_color"],"data":{"line_color":["#000003","#000003","#000003","#000003","#550F6D","#550F6D","#BA3655","#F98C09","#F98C09","#F98C09","#FCFEA4"],"xs":[[0,0],[-1,0],[0,0],[1,0],[-1,0],[0,0],[1,1],[-1,1],[0,1],[1,1],[0,0]],"ys":[[0,0],[-1,0],[-1,0],[-1,0],[-2,-1],[-2,-1],[-2,-1],[-3,-2],[-3,-2],[-3,-2],[-4,-3]]}},"id":"dc1cee8d-890a-4ad1-8b70-4789a561b611","type":"ColumnDataSource"},{"attributes":{},"id":"cefea559-1c84-44e2-b196-7501819acbd0","type":"BasicTicker"},{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"23ca301c-d79c-43a3-ba8b-62f117fd7e30","subtype":"Figure","type":"Plot"},"ticker":{"id":"2ca0fdeb-383c-4ae9-b106-a7808ae3e42f","type":"BasicTicker"}},"id":"db8d9cb9-4129-417a-b41e-33662896894a","type":"Grid"},{"attributes":{"overlay":{"id":"c364622e-5065-47f5-9b79-92a9786bbf07","type":"BoxAnnotation"}},"id":"a7255a00-1ca2-454d-b676-878904c0e140","type":"BoxZoomTool"},{"attributes":{},"id":"f125d9ee-761b-4de1-8436-640591a867d8","type":"HelpTool"},{"attributes":{"formatter":{"id":"571e954b-7cea-44e9-a369-ed9be4b03922","type":"BasicTickFormatter"},"plot":{"id":"23ca301c-d79c-43a3-ba8b-62f117fd7e30","subtype":"Figure","type":"Plot"},"ticker":{"id":"2ca0fdeb-383c-4ae9-b106-a7808ae3e42f","type":"BasicTicker"},"visible":false},"id":"a841b1e1-2c32-4839-98e6-e204ecc98ebd","type":"LinearAxis"},{"attributes":{},"id":"2ca0fdeb-383c-4ae9-b106-a7808ae3e42f","type":"BasicTicker"},{"attributes":{"plot":null,"text":"Demo"},"id":"432f38af-31bd-4e71-adec-56abc1403948","type":"Title"}],"root_ids":["23ca301c-d79c-43a3-ba8b-62f117fd7e30"]},"title":"Bokeh Application","version":"0.12.13"}}';
        var render_items = [{"docid":"94bdca91-0cfe-4e2e-9186-020b0d9e9f2d","elementid":"68b0bdc9-d4bf-485e-b3df-e1a83fb66e9c","modelid":"23ca301c-d79c-43a3-ba8b-62f117fd7e30"}];
        root.Bokeh.embed.embed_items(docs_json, render_items);
      
        }
        if (root.Bokeh !== undefined) {
          embed_document(root);
        } else {
          var attempts = 0;
          var timer = setInterval(function(root) {
            if (root.Bokeh !== undefined) {
              embed_document(root);
              clearInterval(timer);
            }
            attempts++;
            if (attempts > 100) {
              console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing")
              clearInterval(timer);
            }
          }, 10, root)
        }
      })(window);
    });
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();
