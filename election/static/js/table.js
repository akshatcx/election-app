$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        language: dt_language,
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "center",
             targets: [0, 1, 2, 3, 4]
            },
            {
                name: 'vid',
                targets: [0]
            },
            {
                name: 'name',
                targets: [1]
            },
            {
                name: 'Address',
                targets: [2]
            },
            {
                name: 'number',
                targets: [3]
            },
            {
                name: 'gender',
                targets: [4]
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: TESTMODEL_LIST_JSON_URL
    });
});
