$( document ).ready(function() {
    $('#addModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus')
      })
});

