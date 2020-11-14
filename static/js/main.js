window.onload = function () {
    let notyf = new Notyf({
        duration: 2000,
        position: {
            x: 'right',
            y: 'top',
        },
    });
    $('.add').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (data) {
                if (data) {
                    $('span').addClass('badge-primary');
                    notyf.success('Успешно добвили в корзину!');
                } else {
                    notyf.error('Ошибка!');
                }

            }
        })
    })
    $('.basket_remove').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (data) {
                if (data) {
                    notyf.success('Успешно удалили!');
                    $('.col').hide('1000').remove();
                    $('span').removeClass('badge-primary');
                } else {
                    notyf.error('Ошибка!');
                }
            }
        })
    })
}