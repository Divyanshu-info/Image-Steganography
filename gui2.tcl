#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Nov 17, 2021 06:38:56 PM IST  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 600x461+383+167
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1351 738
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel2" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr66 \
        -borderwidth 2 -relief groove -width 585 -height 446 
    vTcl:DefineAlias "$top.tFr66" "TFrame1" vTcl:WidgetProc "Toplevel2" 1
    set site_3_0 $top.tFr66
    ttk::entry $site_3_0.tEn67 \
        -foreground {} -background {} -takefocus {} -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn67" "TEntry1" vTcl:WidgetProc "Toplevel2" 1
    ttk::entry $site_3_0.tEn68 \
        -foreground {} -background {} -takefocus {} -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn68" "TEntry2" vTcl:WidgetProc "Toplevel2" 1
    ttk::label $site_3_0.tLa69 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -relief flat -anchor w -justify left -text {Input File Name} 
    vTcl:DefineAlias "$site_3_0.tLa69" "TLabel1" vTcl:WidgetProc "Toplevel2" 1
    ttk::label $site_3_0.tLa70 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -relief flat -anchor w -justify left -text Key 
    vTcl:DefineAlias "$site_3_0.tLa70" "TLabel2" vTcl:WidgetProc "Toplevel2" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu71 \
        -command print() -takefocus {} -text ... 
    vTcl:DefineAlias "$site_3_0.tBu71" "TButton1" vTcl:WidgetProc "Toplevel2" 1
    ttk::label $site_3_0.tLa72 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -relief flat -anchor w -justify left -text Tlabel 
    vTcl:DefineAlias "$site_3_0.tLa72" "TLabel3" vTcl:WidgetProc "Toplevel2" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu73 \
        -command print() -takefocus {} -text Decode 
    vTcl:DefineAlias "$site_3_0.tBu73" "TButton2" vTcl:WidgetProc "Toplevel2" 1
    place $site_3_0.tEn67 \
        -in $site_3_0 -x 0 -relx 0.205 -y 0 -rely 0.022 -width 414 \
        -relwidth 0 -height 23 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn68 \
        -in $site_3_0 -x 0 -relx 0.205 -y 0 -rely 0.09 -width 414 -relwidth 0 \
        -height 23 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa69 \
        -in $site_3_0 -x 0 -relx 0.017 -y 0 -rely 0.022 -width 0 \
        -relwidth 0.185 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa70 \
        -in $site_3_0 -x 0 -relx 0.137 -y 0 -rely 0.09 -width 0 \
        -relwidth 0.048 -height 0 -relheight 0.047 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu71 \
        -in $site_3_0 -x 0 -relx 0.923 -y 0 -rely 0.022 -width 33 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa72 \
        -in $site_3_0 -x 0 -relx 0.017 -y 0 -rely 0.157 -width 0 \
        -relwidth 0.954 -height 0 -relheight 0.697 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu73 \
        -in $site_3_0 -x 0 -relx 0.427 -y 0 -rely 0.919 -width 83 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tFr66 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.022 -width 0 -relwidth 0.975 \
        -height 0 -relheight 0.967 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

