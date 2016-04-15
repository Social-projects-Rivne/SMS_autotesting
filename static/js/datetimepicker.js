$(function () {
    $('#datetimepicker').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: moment.locale('uk'),
        daysOfWeekDisabled: [0,6]
    }).on('dp.hide', function(event){
        $(this).blur();
    });
});