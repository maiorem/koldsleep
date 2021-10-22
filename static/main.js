//Popup Module
const popup = function() {
    var $pop;
    var $btn;
    var popMode;

    function createPopup(popId) {
        var popWrap = '<div id="'+ popId +'" class="pop-modal" data-mode="create"><div class="pop-overlay"></div></div>';
        $("body").append(popWrap);
    }

    var popupFn = {
        open: function(mode, btn, target, callback) {
            if (mode == "inline") {
                $btn = $(btn);
                popMode = mode;
                $pop = $(target);

                $pop.attr("data-mode","inline");

                $pop.stop().fadeIn('fast', function(){
                    if (callback){
                        eval(callback);
                    }
                });

            } else if (mode == "create") {
                $btn = $(btn);
                popMode = mode;

                if (target) {
                    createPopup(target);

                    $pop = $('#' + target);

                    $pop.attr("data-mode","create");

                    if (callback) {
                        console.log(callback);
                        var html = eval(callback);

                        $pop.find(".pop-overlay").append(html);

                        $pop.stop().fadeIn('fast', function(){

                        });
                    }
                }

            }
        },
        close: function(closeBtn, target, callback) {

            if (closeBtn) {
                $pop = $(closeBtn).closest(".pop-modal");
            } else if (target) {
                $pop = $(target);

            } else {
                $pop = $(".pop-modal:visible:last-child");
            }

            $pop.stop().fadeOut('fast', function() {
                if (popMode == "create") {
                    $pop.remove();
                }

                if (callback){
                    eval(callback);
                }
            });
        }
    }

    $(document).on('click', '.btn-pop-open', function(e) {
        e.preventDefault();
    });

    $(document).on('click', '.btn-pop-close', function(e) {
        var $closePop = $(this).closest(".pop-modal");

        popupFn.close(this, $closePop);
    });

    // Click Overlay
    $(document).on('click', '.pop-modal', function(e){
        if ($(this).find(".pop-wrapper").has(e.target).length === 0){
            popupFn.close();
        };
    });

    // Esc Key Popup Close
    $(document).keydown(function(e){
        if (e.keycode == 27 || e.which == 27) {
            popupFn.close();
        }
    });

    return {
        open: popupFn.open,
        close: popupFn.close
    }
};

window.pop = popup();

//Popup Event
jQuery(document).ready(function(e){


    // Popup Open
    $(document).on('click', '[data-popup-open]', function(e) {
        var targeted_popup = $(this).attr('data-popup-open');
        var popup = $('[data-popup="' + targeted_popup + '"]');
    
        $(".chat-discussion").addClass("popmode");
    
        popup.fadeIn(350);
        popup.find('textarea').focus();
        e.preventDefault();
    });

    $(document).on('click', '[data-popup-close]', function(e) {
        var targeted_popup = $(this).attr('data-popup-close');
    
        $('[data-popup="' + targeted_popup + '"]').fadeOut(350, function(){
            $(".chat-discussion").removeClass("popmode");
        });
        e.preventDefault();
    });
});

/********************************************************** element *************************************************************************************/
var loadEl = {
    'pop_del_confirm': function(msg) {
        var html = '<div class="pop-wrapper pop-round pop-noHead pop-reason">' +
                        '<div class="pop-container">' +
                            '<div class="pop-content">' +
                                '<section class="section">' +
                                    '<div class="section-message">' +
                                        msg +
                                    '</div>' +
                                '</section>' +
                            '</div>' +
                            '<div class="pop-footer">' +
                                '<button type="button" id="btnDelete" class="btn btn-primary">삭제</button>' +
                                '<button type="button" onclick="pop.close(this);" class="btn btn-secondary">취소</button>' +
                            '</div>' +
                        '</div>' +
                    '</div>';

        return html;
    },'pop_reg_confirm': function(msg) {
        var html = '<div class="pop-wrapper pop-round pop-noHead pop-reason">' +
                        '<div class="pop-container">' +
                            '<div class="pop-content">' +
                                '<section class="section">' +
                                    '<div class="section-message">' +
                                        msg +
                                    '</div>' +
                                '</section>' +
                            '</div>' +
                            '<div class="pop-footer">' +
                                '<button type="button" onclick="pop.close(this);" class="btn btn-secondary">취소</button>' +
                                '<button type="button" id="btnReg" class="btn btn-primary">등록</button>' +
                            '</div>' +
                        '</div>' +
                    '</div>';

        return html;
    },
    'pop_alert': function(msg) {
        var html = '<div class="pop-wrapper pop-round pop-noHead pop-reason">' +
                        '<div class="pop-container">' +
                            '<div class="pop-content">' +
                                '<section class="section">' +
                                    '<div class="section-message">' +
                                        msg +
                                    '</div>' +
                                '</section>' +
                            '</div>' +
                            '<div class="pop-footer">' +
                                '<button type="button" onclick="pop.close(this);" class="btn btn-primary">확인</button>' +
                            '</div>' +
                        '</div>' +
                    '</div>';

        return html;
    }

}