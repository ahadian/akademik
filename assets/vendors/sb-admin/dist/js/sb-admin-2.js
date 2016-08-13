$(function() {

    $('#side-menu').metisMenu();

});

//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function() {
    $(window).bind("load resize", function() {
        topOffset = 50;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    var element = $('ul.nav a').filter(function() {
        return this.href == url;
    }).addClass('active').parent().parent().addClass('in').parent();
    if (element.is('li')) {
        element.addClass('active');
    }
});

/*$(function () {
    var Row = document.getElementById("data-nilai");
    var Cells = Row.getElementsByTagName("td");
    var i;

    var oTable = document.getElementById('data-nilai');
    var panjangRow = oTable.rows.length;

    for (i=1; i < panjangRow; i++)
        {
            var oCells = oTable.rows.item(i).cells;
            if (modify == oCells[0].firstChild.dataset){
                document.getElementById("Error").innerHTML = "  * duplicate value";
                return false;
                break;
            }
            var hapus = Row.getElementById("hapus");
            if (hapus.onclici].innerText)
            }k == true)
            {
                alert(hapus[i].innerText)
            }
    }
    //alert(Cells[0].innerText);
});*/

$('#editModal').on('show.bs.modal', function (event) {

    var button = $(event.relatedTarget) // Button that triggered the modal
    var id = button.data('id') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)

    var nis = button.data('nis')
    var nama = button.data('nama')
    var kelas = button.data('kelas')
    var mapel = button.data('mapel')
    var semester = button.data('semester')
    var harian = button.data('harian')
    var uts = button.data('uts')
    var uas = button.data('uas')
    var tahun = button.data('tahun_ajaran')

    $(".modal-body #nis").text(nis).val(nis)
    $(".modal-body #nama").text(nama).val(nama)
    $(".modal-body #kelas").text(kelas).val(kelas)
    $(".modal-body #mapel").text(mapel).val(mapel)
    $(".modal-body #semester").text(semester).val(semester)
    $(".modal-body #harian").text(harian).val(harian)
    $(".modal-body #uts").text(uts).val(uts)
    $(".modal-body #uas").text(uas).val(uas)
    $(".modal-footer #id_raport").text(id).val(id)
    $(".modal-footer #nis").text(id).val(nis)
    $(".modal-body #tahun_ajaran").text(tahun).val(tahun)



    //modal.find('.modal-body input"').val(nis)
    //modal.getElementById(modal.id('nis')).valueOf(nis)


});

$('#delModal').on('show.bs.modal', function (event) {

    var button = $(event.relatedTarget)
    var modal = $(this)
    var id_raport = button.data('id')
    var nis = button.data('nis')

    $(".modal-body #text").text('Ingin menghapus data '+nis)
    $(".modal-footer #id_raport").text(id_raport).val(id_raport)

});

