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
                    notyf.success('Успешно добавили в корзину!');
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
                } else {
                    notyf.error('Ошибка!');
                }
            }
        })
    })
    // $('.edit').on('click', function (e) {
    //     e.preventDefault();
    //     $.ajax({
    //         url: e.target.href,
    //         success: function (data) {
    //             if (data) {
    //                 notyf.success('Успешно изменили данные!');
    //             } else {
    //                 notyf.error('Ошибка!');
    //             }
    //
    //         }
    //     })
    // })
    // $('.edit').on('click', function (e) {
    //     e.preventDefault();
    //     notyf.error('В данный момент это не возможно сделать!')
    // })
}