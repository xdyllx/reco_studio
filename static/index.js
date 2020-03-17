$('#table').bootstrapTable({
    striped: true,
    search: true,
    pagination: true,
    pageNumber: 1,
    pageSize: 10,
    columns: [{
        field: 'item_id',
        title: 'item_id'
    }, {
        field: 'item_type',
        title: 'item_type'
    }]
});


$('.card-title').click(function () {
    var index = $(this).attr('name');
    alert(index);
});

$('#send_request_button').click(function () {
   $.get('send_request/', function (ret) {
           if (ret.status == 0) {
               $('#process_content').html(ret.info_list_render);
               $('#table').bootstrapTable('load', ret.result_list[ret.result_list.length-1]);
               window['result_list'] = ret.result_list;
           } else {
               // todo
               // showToastr('error', 'unknown error');
           }
        });
});