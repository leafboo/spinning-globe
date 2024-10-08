import time
import curses
from curses import wrapper

# This comment is just for a commit to push to github to fix not successful push in my linux setup


globe = [""" 
              _-o#&&*''''?d:>b)_
          _o/"`''  '',, dMF9MMMMMHo_
      .o&#'        `"MbHMMMMMMMMMMMHo.
    .o"" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH)
  /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             ""*"'""*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
  :9MMk                    `MMM#"        -
    &M}                     `          .-
      `&.                             .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp=""'
      """,
      """
              _v->#H#P? "':o<>)_
          .,dP` `''  "'-o.+H6&MMMHo_
        oHMH9'         `?&bHMHMMMMMMHo.
      oMP"' '           ooMP*#&HMMMMMMM?.
    ,M*          -     `*MSdob//`^&##MMMH)
  d*'                .,MMMMMMH#o>#ooMMMMMb
  HM-                :HMMMMMMMMMMMMMMM&HM[R)
d"Z).               9MMMMMMMMMMMMMMMMM[HMM|:
-H    -              MMMMMMMMMMMMMMMMMMMbMP' :
:??Mb#               `9MMMMMMMMMMMMMMMMMMH#! .
: MMMMH#,              "*"'""`#HMMMMMMMMMMH  -
||MMMMMM6).                    {MMMMMMMMMH'  :
:|MMMMMMMMMMHo                 `9MMMMMMMM'   .
. HMMMMMMMMMMP'                 !MMMMMMMM    `
- `#MMMMMMMMM                   HMMMMMMM*,/  :
 :  ?MMMMMMMF                   HMMMMMM',P' :
  .  HMMMMR'                    {MMMMP' ^' -
  : `HMMMT                     iMMH'     .'
    -.`HMH                               .
      -:*H                            . '
        -`),,    .                  .-
          ' .  _                 .-`
              '`~).__,obb#q==~'''
    """,
    """
              .ovr:HMM#?:`' >b)_
          .,:&Hi' `'   "' )|&bSMHo_
        oHMMM#*}          `?&dMMMMMMHo.
    .dMMMH"''''           ,oHH*&&9MMMM?.
    ,MMM*'                 `*M)bd<|"*&#MH)
  dHH?'                   :MMMMMM#bd#odMML
  H' |)                  `dMMMMMMMMMMMMMM9Mk
JL/"7+,.                `MMMMMMMMMMMMMMMH9ML
-`Hp     '               |MMMMMMMMMMMMMMMMHH|:
:  )#M#d?                `HMMMMMMMMMMMMMMMMH.
.   JMMMMM##,              ``*""'"*#MMMMMMMMH
-. ,MMMMMMMM6o_                    |MMMMMMMM':
:  |MMMMMMMMMMMMMb)                 TMMMMMMT :
.   ?MMMMMMMMMMMMM'                 :MMMMMM|.`
-    ?HMMMMMMMMMM:                  HMMMMMM)|:
 :    9MMMMMMMMH'                  `MMMMMP.P.
  .    `MMMMMMT''                   HMMM*''-
  -    TMMMMM'                     MM*'  -
    '.   HMM#                            -
      -. `9M:                          .'
        -. `b,,    .                . '
          '-)   .,               .-`
              '-:b~)_,oddq==--"
    """,
    """
              _oo##'9MMHb':'-,o_
          .oH":HH$' ""'  "' -)7*R&o_
      .oHMMMHMH#9:          ")bMMMMHo.
      dMMMMMM*""'`'           .oHM"H9MM?.
    ,MMMMMM'                   "HLbd<|?&H)
  JMMH#H'                     |MMMMM#b>bHb
  :MH  .")                   `|MMMMMMMMMMMM&
.:M:d-"|:b..                 9MMMMMMMMMMMMM+
:  "*H|      -                &MMMMMMMMMMMMMH:
.    `LvdHH#d?                `?MMMMMMMMMMMMMb
:      iMMMMMMH#b               `"*"'"#HMMMMMM
.   . ,MMMMMMMMMMb).                   {MMMMMH
-     |MMMMMMMMMMMMMMHb,               `MMMMM|
:      |MMMMMMMMMMMMMMH'                &MMMM,
-       `#MMMMMMMMMMMM                 |MMMM6-
:        `MMMMMMMMMM+                  ]MMMT/
  .       `MMMMMMMP"                   HMM*`
  -       |MMMMMH'                    ,M#'-
    '.     :MMMH|                       .-
      .     |MM                        -
      ` .   `#?..    .             ..'
          -.     _.             .-
              '-|.#qo__,,ob=~~-''
    """,
    """
              _ooppH[`MMMD::--)_
          .oHMMMR:"&MZ) `"'  "  |$-_
      ..dMMMMMMMMdMMM#9)        `'HHo.
    . ,dMMMMMMMMMMM"`' `           ?MP?.
    . |MMMMMMMMMMM'                 `"$b&)
  -  |MMMMHH##M'                     HMMH?
  -   TTMM|    >..                   )MMMMMH
:     |MM),#-""$~b).                `MMMMMM+
.       ``"H&#        -               &MMMMMM|
:            *)v,#MHddc.              `9MMMMMb
.               MMMMMMMM##)             `"":HM
-          .  .HMMMMMMMMMMRo_.              |M
:             |MMMMMMMMMMMMMMMM#)           :M
-              `HMMMMMMMMMMMMMMM'           |T
:               `*HMMMMMMMMMMMM'            H'
 :                 MMMMMMMMMMM|            |T
  .                MMMMMMMM?'             ./
  `.               MMMMMMH'              ./
    -.            |MMMH#'                .
      .           `MM*                . '
        -.         #M: .    .       .-
          ` .         .,         .-
              '-.-~ooHH__,,v~--`
    """,
    """
              _ood>H&H&Z?#M#b-).
          .)HMMMMMR?`)M6b."`' ''``v.
      .. .MMMMMMMMMMHMMM#&.      ``~o.
    .   ,HMMMMMMMMMMMM*"'-`          &b.
    .   .MMMMMMMMMMMMH'               `"&)
  -     RMMMMM#H##R'                   4Mb
  -      |7MMM'    ?::                 `|MMb
/         HMM__#|`")>?v..              `MMML
.           `"'#Hd|       `              9MMM:
-                |),)?HH#bbL             `9MMb
:                   !MMMMMMMH#b,          `""T
.              .   ,MMMMMMMMMMMbo.           |
:                  4MMMMMMMMMMMMMMMHo        |
:                   ?MMMMMMMMMMMMMMM?        :
-.                   `#MMMMMMMMMMMM:        .-
 :                     |MMMMMMMMMM?         .
  -                    JMMMMMMMT'          :
  `.                   MMMMMMH'           -
    -.                |MMM#*`            -
      .               HMH'            . '
        -.            #H:.          .-
          ` .           .)       .-
              '-..-+oodHL_,--/-`
    """,
    """
              _,)?dZkMHF&$*q#b..
          .//9MMMMMMM?:'HM)"`-''`..
      ..`  :MMMMMMMMMMHMMMMH?_    `-)
    .     .dMMMMMMMMMMMMMM'"'"       `).
    .      |MMMMMMMMMMMMMR              )
  -        T9MMMMMHH##M"                `?
  :          (9MMM'    !':.               &k
.:            HMM)_?p "":-b).            `ML
-                "'"H&#,       :           |M|
:                     ?),)dMH#b#.           9b
:                        |MMMMMMM##,        `*
:                   .   +MMMMMMMMMMMo_       -
:                       HMMMMMMMMMMMMMM#,    :
:                        9MMMMMMMMMMMMMH'    .
: .                       *HMMMMMMMMMMP     .'
 :                          MMMMMMMMMH'     .
  -                        :MMMMMMM'`      .
  `.                       9MMMMM*'       -
    -.                    {MMM#'         :
      -                  |MM"          .'
      `.                &M'..  .   ..'
          ' .             ._     .-
              '-. -voboo#&:,-.-`
    """,
    """
              _oo:)bk99M[<$$+b).
          .$*"MMMMMMMM[:")Mb)?^" .
      . '`    HMMMMMMMMMMHMMMM+?.  `.
    .        .HMMMMMMMMMMMMMMP"''     .
    .         `MMMMMMMMMMMMMM|         -`.
  -           `&MMMMMMHH##H:             :
  :             `(*MMM}    `|)             |
: `-              ?MMb__#|""`|+v..         )
.                    `''*H#b       -        :|
:                         `*)v,#M#b#,        )
.                             9MMMMMMHb.     :
:                        .   #MMMMMMMMMb)    -
-                           .HMMMMMMMMMMMMb  :
:                            `MMMMMMMMMMMMH  .
-:  .                         `#MMMMMMMMMP   '
 :                              ]MMMMMMMH'  :
  -                            ,MMMMMM?'   .
  `:                           HMMMMH"    -'
    -.                       .HMM#*     .-
    `.                     .HH*'     .
      `-.                  &R".    .-
          -.               ._   .-
              '-. .voodoodc?..-`
    """,
    """
              _)oo)?ddk9MRbS>v)_
          ..:>*""MMMMMMMMM:?|H?$?-.
      ..- -     "HMMMMMMMMMMHMMMH)_-.
    .            dMMMMMMMMMMMMMMT"    .
    .             TMMMMMMMMMMMMMM       `.
  -               `&HMMMMMM#H#H:         .
  -                 `)7HMMH     |).        .
:    `                 HMM)_?c`""+?)..     :
-                         "``#&#|      .     -
:                              `?,)#MHdb.    .
:                                 |MMMMMH#.  :
:                            .   ,HMMMMMMMb, -
: '                              4MMMMMMMMMMH`
:   .                             9MMMMMMMMMT-
:.`                               `#MMMMMMMH '
 :      '                           HMMMMMH':
  -                                |MMMMH" -
  `:                              |MMMH*' .'
    '?                           dMM#'   .
      ).                       .dH"    .'
        -.                    ,M'-  ..'
          ` .                .. ..-`
              '-. .)ooooboo<^.-`

    """,
    """
              _o,:o?)?dM&MHcc~,.
          ..^':&#""HMMMMMMMM$:?&&?.
        .`  -`      'HMMMMMMMMMHMMMp).
    . '             |MMMMMMMMMMMMMM"' .
    .                `9MMMMMMMMMMMMM    -.
  -                   `*9MMMMMHH##[      .
  -                     `)Z9MMM    `~)     .
:       '|                 ?MMb_?p""-?v..  :
-                             `"'*&#,    -   .
:                                  `?,oHH#?  .
--                                    |MMMMH,:
:                                 .  |MMMMMM6,
:   -                                |MMMMMMMM
?                                     HMMMMMMP
-- . '                                |HMMMMM'
 :.`     .  '                          JMMMM+
  )                                   ,MMMP:
  :                                 |MMH?:
    -:).                            dM#" .
      )                          ,H*' .'
        -.                       d':..'
          ` .                  .,.-
              '-.. .)oooodov~^-`
    """,
    """
              _o):,??)??MR9#cb)_
          .v/''':&#""#HMMMMMMM$?*d).
      ..~' - -`      `"#MMMMMMMMMMMHv.
    .-'                 HMMMMMMMMMMMR!.
    :                    `9MMMMMMMMMMM| -.
  .                       `*9MMMMMH##|   .
  -                          `(#MMH   `:,  .
:           '|                 `HMb_>/"|),.:
.'                                `"'#&b   - .
:                                      ?)oHH?.
:                                        !MMM&
:  .                                  .  HMMMM
/.      -                               -MMMMM
)`.                                      9MMMP
:. .  . -                                |MMM'
 )... '                                  .MMT
  &.                                    .dMP
  ),                                  .HM*
    ). `).                            ,H&'
    `- `| -                        ,&':
      `.                         ,/) '
          '-..                  _.-
              "---.._)o,oov+--'"

    """,
    """
              _,d?,:?o?:?HM>#b)_
          ..H*"''`'H#*"**MMMMMM6$$v_
        v//"   - ``      `'#MMMMMMMMHo.
      /"`                   |MMMMMMMMMM:.
    ,>                       `HMMMMMMMMH:.
  :                           `#HMMMMHH) -
  '                              `Z#MM,  `,:
:               ')                 ?HH_>:`),
:                                     "'*&| `:
.                                         <)Hb
:                                           MM
:                                        . iMM
Mb).                                       {MM
::.`-       -                              !MP
`&.   .  .  -                              :M'
 9H,  )  '                                 |T
  HM?                                     ,P
  *ML                                   ??
    :&.   `o                           .d'
      ':  |T                          /"
        -.                         .<''
          `...                  ..-
              "`-=.,_,,,oov-~.-`
    """,
    """
              _,oc>?_:b?o?HH#b)_
          .v/99*"'" '*H#""*HMMMMMZ,_
        oH* /"   -   '      "`#MMMMM#o.
     ./*>-                     `MMMMMMMb
    ,b/'                        `#MMMMMMM)
   :'                             ``HMMMMb:
  /-                                `|&MH `)
 /                   `-.               |Hb??)
,-  '                                    "`&,.
1                                           )}
!.                                           T
$,.                                        . 1
?`M??.                                       M
?.::| ')        -                            ?
 M?&.    .   .  -                           ,'
 9MMH)   ..  '           `                  .
  HMMM#.                                   :'
   9#MMb                                 ..
    -:"#     `b.                        .-
      . `    {!                        /
        -                           ,-'
          ' .                    .-
             ```^==)_.,,,ov--)-`

    """,
    """
              _)o##??,:io??$#b)_
          .oH#"H9*"'" "`#H*"*#MMMHo_
        oHMM- -'    -  ''     ``*HMMHo.
      dM#S>-`                     ?MMMM?.
    ,&&,/'                         "#MMMH)
   d?-"                              `*HMMb
  H?                                   "ZHb:
 /:                        )              H?L
|:|   .                                    `*:
:?:                                          )
>"                                           :
M|),_                                        |
!|":HH?-'.                                   :
:^'_:?") `--         -                       .
- |ML?b      .   ..  -                       -
 :HMMMMH)    )               `              :
  >MMMMMM#.                                .
   ^M*HMMM|                               -
    `. `"#+     `?v                     .`
      .   `-    +?'                    -
       ` .                          ..'
           - .                   .-
              "`)b=p?.._)vv---`
    """,
    """
              _,o#bH)??::?o?cbo_
          .o#MH#**SH""' "`*H#"*#MHo_
        oHMMMH^  ^"    -  `      '*HHo.
     .dMMM#">>-                     `HM?.
    ,MH:R_o/                         `*MH)
   dMM' '                               "ML
  HMR! '                                 `#k
 d&'.                          -.          `L
:M ::     `                                 `-
/| !|                                        -
k.$-"                                        :
}9R:!,,_.                                    .
)::)':`*M#)-'.                               -
: "''..:"!`)  '-          -                  `
-   ,HMb.H|      .    _   -                 .'
 : ,MMMMMMMb.    ..                         .
  .`HMMMMMMMM?                             .
  `.`9M#*HMMMM                            :
    -.'   "##*      `b,                  .
      .      `     ,/'                 .'
       ` .                          ..'
           - .                  ..-
              "`*#d##c.._)v----`
    """,
    """
              _,o#&oHb?)o::d?>)_
          .oHHMMM#**$M""` "`*HH"#&o_
        oHMMMMMMD' .''    -  '    ``bo.
     .dMMMMMH*'/|-                   `)b.
    ,MMMM?T|_o/                        `)
   dMMMMP  ''                            `|
  HMMMH& -                                `)
 /MH7' :                          --        :
-:MM  {.      .                              .
:i?' .!&                                     .
:{, o| '                                     :
-T?9M):-'o,_                                 .
: )?::``"`?9MHo./..                          -
.  '"`'^ _.`"!"^.  `-         -              `
-      ,bMM?.M)       .    .  -      .      .'
 :   .oMMMMMMMMb.    ..   `                 .
  .  `HMMMMMMMMMMb                         -
   -   9MH*#HMMMMH                        .'
    '.  '   `"*##'      `b.              :
      .         `     .d''             .'
        -.                          . '
           -.                    .-`
              "`*##H###:._)--.-`
    """,
    """
              _oo#H&d#b?)b:_>>)_
          .oHMMMMMMH*"*9R"'-``*#P)-_
        oHMMMMMMMMM$  ."       '   `^-
     .dMMMMMMMMH*",?-                 ').
    ,MMMMMMM:?}.,d'                     `.
   dMMMMMMMH  /''                         :
  HMMMMMMM&' -                             -
 dPTMMP>' :                           -.    :
|? -MM}  .)                                  .
J' ::*'  -$L                                 .
:  ?b .,H- '                                 :
-  |6.&MP:: !.,_.                            -
:   `):: "' "`:"MM#,-^,            -         :
-     ````:' _.:"?``)   `-                   .
:         .?bMML.]#        -   _  `      .  .'
 -      .o#MMMMMMMMH)     ).          .     .
  -     `HMMMMMMMMMMMH                     :
  `.     `HMM#*#MMMMMH'                   -
    -.     '    ``##*'      i+           :
      -            `'     v/'          .'
       `-                           ..'
          ' .                    .-
              "`*##HMH##:__,-.-`
    """,
    """
              _oo##Mbb&bo??o_>)_
          .oHMMMMMMMMM**#?M*' "?*&..
        oHMMMMMMMMMMMM4  `"      -  `.
     .dMMMMMMMMMMMM#")?.-              .
    ,MMMMMMMMMM}"9:_,d'                 -.
   dMMMMMMMMMMM|  ^''                     .
  &MMMMMMMMMMH)  -                         .
 :{M*"MMMPT"' :                         `-. :
.'M'  'MMM.  -T,       .                     .
- k   i:?''  -|&                             .
: `  -o&  .,H- "                             :
-     `M:`HMP|:'!.o._.                       .
:      "<:::'<^ '"``9MH#,-^ .                -
-         '''``''._.`"?`^|   ^        -      :
:              ?#dMM_.M?       .   .  -    ..'
 :          ,ddMMMMMMMMMb.    ..   '        .
  .         TMMMMMMMMMMMMM,                :
   -         ?MMH**#MMMMMH'               :
    '.        '     "`##*'      &.       :
      -.               `'    ,~"       .'
        -.                          ..'
          ` .                    .-
             ```*##HMMMH#<:,..-`
    """,
    """
              _,dd#HMb&dHo?)?:)_
          .oHMMMMMMMMMMMH***9P'`")v.
        oHMMMMMMMMMMMMMMM>  `'      -.
     .dMMMMMMMMMMMMMMMH*'|~-'          .
    ,MMMMMMMMMMMMM6>`H._,&              -.
   dMMMMMMMMMMMMMMM|  `"                  .
  H*MMMMMMMMMMMMMH&. -                     .
 d' HMM""&MMMPT'' :.                      `.-
,'  MP   `TMMM,   |:        .                -
|   #:    ? *"   : &L                        :
!   `'   /?H   ,#r `'                        :
.         ?M: HMM^<~->,o._                   :
:          `9:::'`*-``':`9MHb,|-,         '  :
.             `"''':' :_ ""!"^.  `|          :
`.                 _dbHM6_|H.      .   . '  .'
 )              _odHMMMMMMMMH,    ..  `     :
 `-             |MMMMMMMMMMMMM|            :
  `.             9MMH**#MMMMMH'           :
    -.            '     "?##"      d     :
      .                    '    ,/"    .'
       `..                          ..'
          `  .                   .-
              '`"#HHMMMMM#<>..-`
    """,
    """
              _oo##bHMb&d#bd,>)_
          .oHMMMMMMMMMMMMMM***9R"-..
        oHMMMMMMMMMMMMMMMMMH)  ?   `-.
     .dMMMMMMMMMMMMMMMMMMM#".}-'       .
    ,MMMMMMMMMMMMMMMMM6/`H _o}          -.
   dMMMMMMMMMMMMMMMMMMML  `''             .
  HbP*HMMMMMMMMMMMMMMM*: -                 ,
 dMH' `MMMP'"HMMMR'T"  :                    :
|H'   -MR'   `?MMMb    P,       .            .
1&     *|     |.`*"  .-`&|                   .
M'      "    |)&|  .,#~ "'                   :
T             :HL.|HMH)c~`|v,)_              :
|              `"|:::':`-`` '"MM#)-'.       -:
%                 ``'``'`' :_ '?'`| ``.      :
||,                     ,#dMM?.M?      .  .` -
 ?)                 .,odMMMMMMMMM?    )  `  :
  /                 |MMMMMMMMMMMMM:        .'
  `.                 TMMH#*9MMMMM*        :
    -.               `      "*#*'    ,:  .
      .                       `   .v'' .'
       `.                           ..'
          '- .                   .-
              "`)+HHMMMMMMHr~.-`
    """,
    """
             _,,>#b&HMHd&&bb>)_
          _oHMMMMMMMMMMMMMMMMH**H:.
        oHMMMMMMMMMMMMMMMMMMMM#v`?  `.
     .dMMMMMMMMMMMMMMMMMMMMMMH*`+|     .
    ,MMMMMMMMMMMMMMMMMMMMMb|?+.,H       -.
   ddHMMMMMMMMMMMMMMMMMMMMMb  `'          .
  HMMkZ**HMMMMMMMMMMMMMMMMH)  -   .        :
 dTMMM*  `9MMMP'"*MMMMPT"` ..               :
|M6H''    4MP'   `"HMMM|   !|.      .        .
1MHp'      #L      $ *"'  .-:&.              .
MMM'        "     q:H.  .o#-``'              :
MM'                ?H?.|MMH::::-o,_.         -
M[                  `*?:::'|` `"`:9MH)~-.    `
&M.                     ""'`'^'.:.`?'`. '|  -:
`M|d,                       .dbHM[.1?     .. :
 9||| .                  _obMMMMMMMMH,   .  :
  H.^                    MMMMMMMMMMMM}     -
   )                     |MMH#*HMMMMH'    .'
    .                    `      `#*'   ,:-
     `                           '' .-'.
       `.                           .-
          '- .                   .-`
              '`)bqHMMMMMMHHb--`

    """,
    """
              .,:,#&6dHHHb&##o)_
          .oHHMMMMMMMMMMMMMMMMMH*),.
        oHMMMMMMMMMMMMMMMMMMMMMMHb:'-.
     .dMMMMMMMMMMMMMMMMMMMMMMMMMH|)/'  .
    ,&HMMMMMMMMMMMMMMMMMMMMMMM/"&.,d.   -.
   dboMMHMMMMMMMMMMMMMMMMMMMMMML `'       .
  HMHMMM$Z***MMMMMMMMMMMMMMMMMM|.-         .
 dMM}MMMM#'  `9MMMH?"`MMMMR'T'  _           :
|MMMbM#''     |MM"    ``MMMH.   <_           .
dMMMM#&        *&.     .?`*"   .'&:          .
MMMMMH-         `'    -v/H   .dD "'  '       :
MMMM*                  `*M: 4MM*::-!v,_      :
MMMM                     `*?::" "'``"?9Mb::. :
&MMM,                       `"'"'|"._ "?`| - :
`MMM}.H                          ,#dM[_H   ..:
 9MMi`M: .                   .ooHMMMMMMM,  ..
  9Mb `-                     1MMMMMMMMMM|  :
   ?M                        |MM#*#MMMM*  .
    -.                       `     |#"' ,'
      .                            -" v`
        -.                          .-
           - .                   . `
              '-*#d#HHMMMMHH#"-'

    """,
    """
              _,<_:&S6dHHHb&bb)_
          .odHMMMMMMMMMMMMMMMMMMM}-_
       .oHMMMMMMMMMMMMMMMMMMMMMMMM#d:.
      ?9MMMMMMMMMMMMMMMMMMMMMMMMMMMH-$ .
    ,::dHMMMMMMMMMMMMMMMMMMMMMMMMH:).?? -.
   dMdboHMMHMMMMMMMMMMMMMMMMMMMMMMH, '    .
  HMMMM7MMMb$R***MMMMMMMMMMMMMMMMMH) -     .
 dMMMMM/MMMMM*   `$MMMM*'"*MMMM?&'  .       :
|MMMMMMb1H*'       HMP'    '9MMM|   &.    .  .
dMMMMMMM##~`       `#)      |.`*"  .-9.      :
9MMMMMMMM*           `     |v7?  .,H `' `    :
SMMMMMMH'                   '9M_-MMH::-)v_   :
:HMMMMM                       `)_:"'|'`':9Mv).
-|MMMMM,                         ""`'`':.`?) )
`:MMMMM}.d}                         .?bM6,|  |
 :?MMM6  M|  .                   .,oHMMMMM| /
  .?MMM- `'                      &MMMMMMMM|.
   -`HM-                         HMH#*MMM?:
    '.                           '   `#*:`
      -                              -'/
       ` .                          . '
          ` .                    . `
              '--##HH#HMMMHH#""`

    """,
    """
              _o,d_?dZdoHHHb#b)_
          .vdMMMMMMMMMMMMMMMMMMMMH).
       .,HHMMMMMMMMMMMMMMMMMMMMMMMMH&,.
      /?RMMMMMMMMMMMMMMMMMMMMMMMMMMMMH|..
    ,)?>`T#RMMMMMMMMMMMMMMMMMMMMMMMM6`)|/
   dMMbd#ooHMMMHMMMMMMMMMMMMMMMMMMMMMH,`' '
  HMMMMMMMTMMMMb$ZP**HMMMMMMMMMMMMMMMM|.   :
 dMMMMMMMM}$MMMMMH'   `HMMMH?"`MMMM?T' .    :
|MMMMMMMMMMoMH*''      `MM?    ``MMM|  +)    .
1MMMMMMMMMMMb#/         ?#?      |`#"  -T:   :
*'HMMMMMMMMMM*'           "     ~?&  .?} ' ' .
- 4MMMMMMMMP"                    `M? HMTc:).:
: `MMMMMMM[                       "#:::`>`"?M{
.  |MMMMMMH.                        ``'``'_`:-
-  |MMMMMMM|.dD                         ,#Mb)'
 :  *MMMMM: iM|  .                   _oHMMMM:
  .  ?MMMM'  "'                     ,MMMMMMP
   :  `HMH                          JM#*MMT
    -.  '                           `   #'
      .                                /
        -.            -              .'
           -.                    . `
              '--=&&MH##HMHH#"'"
    """,
    """
              .-:?,Z?:&$dHH##b)_
           ,:bqRMMMMMMMMMMMMMMMMMHo.
        .?HHHMMMMMMMMMMMMMMMMMMMMMMMHo.
      -o/*M9MMMMMMMMMMMMMMMMMMMMMMMMMMMv
    .:H)b)'|?#HHMMMMMMMMMMMMMMMMMMMMMM6?Z)
   .?MMMHbdbbodMMMMHMMMMMMMMMMMMMMMMMMMM)':
  :MMMMMMMMMMM7MMMMb?6P**#MMMMMMMMMMMMMMM_ :
 )MMMMMMMMMMMMb^MMMMMM?   `*MMMM*"`MMMR<' . -
.1MMMMMMMMMMMMMb]M#""       9MR'   `?MMb  ). :
-MMMMMMMMMMMMMMMH##|`        *&.     |`*' .) .
-?""*MMMMMMMMMMMMM'            '    |?b  ,}" :
:    MMMMMMMMMMH'                    `M_|M}r)?
.    `MMMMMMMMM'                      `$_:`'"H
-     TMMMMMMMM,                        '"``::
:     {MMMMMMMM| oH|                      .#M-
 :    `9MMMMMM' .MP   .                 ,oMMT
  .     HMMMMP'  `'                    ,MMMP
   -     `MMH'                         HH9*
    '.    `                           ` .'
      -                               . '
       ` .               -          .-
          ` .                    .-
              ' -==pHMMH##HH#"'"
    """,
    """
              _..-:b&::&?&&##bo_
          ...?-#&9MMMMMMMMMMMMMMMHo_
       .. .1&#MMHMMMMMMMMMMMMMMMMMMMHo.
     .  .o/##R9MMMMMMMMMMMMMMMMMMMMMMMM?.
    .- |MSd?|'`$?#HMMMMMMMMMMMMMMMMMMMMMH)
   -  dMMMMHbd##oodMMMM#MMMMMMMMMMMMMMMMMH:
  - JMMMMMMMMMMMMM7HMMMH$SR***MMMMMMMMMMMMb>
 : {MMMMMMMMMMMMMMM`9MMMMMH'  ``HMMM?"*MM[| :
- |MMMMMMMMMMMMMMMMM<MH*''      `MM'   'HM? |.
: `MMMMMMMMMMMMMMMMMM##H-'       `#,  ` |`? /|
.  ?)")")"?HMMMMMMMMMMMMMH'        "    v& .}?  
-       |MMMMMMMMMMMP'                  `H:&H&
i       `9MMMMMMMMMT                    `|?)"?
:         MMMMMMMMMH                      )"`)
:         MMMMMMMMMH-.dH                    ,|
  :        ?MMMMMMM?  {M' .               .dT
  .        ?MMMMMR'  `'                  ,MP'
    -        `HMM#'                     .&*'
    '.        '                         `.
      -                               . '
        `..                         .-'
            -.                   .-`
               '-.==p##HMMHp&#"'"'
    """,
    """
              _v---:?&?:?&?&#b)_
          ..' i: #M$MMMMMMMMMMMMMHo_
       ..   -]M#HMHMMMMMMMMMMMMMMMMMHo.
     .     ooP*&6&MMMMMMMMMMMMMMMMMMMMM?.
    . -   &Rbbd-/`?:##HMMMMMMMMMMMMMMMMMH?
   -    ,HMMMMM#od#boodMMMMHMMMMMMMMMMMMMMb
  -   iMMMMMMMMMMMMMMM[*MMMH&$R***MMMMMMMMMb
 :   |MMMMMMMMMMMMMMMMML"MMMMMM'  ``MMMP"HMM:
.    HMMMMMMMMMMMMMMMMMMb/MH)")"    `MR   *M,|
:    TMMMMMMMMMMMMMMMMMMMMd#&`       `D.   ?|)
.     `*)"')"*HMMMMMMMMMMMMMMP'        '  -d,J
:           |MMMMMMMMMMMMP'                ||M
M,           ?MMMMMMMMMM|                  `)?
&|            HMMMMMMMMM}                   ``
`L           .MMMMMMMMMMP ,d|                :
 *.           ?MMMMMMMF' .MP                /
  |            TMMMMMM'  `)"'               /
  `.            `MMMP'                   ./
    -.           `                       .
      .                               . '
        - .                         .-'
           -)                   ..-`
              '-..=p####HMH&="'"'
    """,
    """
              _vo~^'':&b::d,#b)_
          ..`" `:v +9P]MMMMMMMMMMHo_
        ,-     ?Mb#MMMMMMMMMMMMMMMMMHo.
     . "     ,ooM*&&&HMMMMMMMMMMMMMMMMHb.
    .   -    99Soo?|'`*?##HMMMMMMMMMMMMMH)
   -       .HMMMMMM#od#boodMMMMHMMMMMMMMMMb
  -      :MMMMMMMMMMMMMMMM67HMMH&$R**HMMMMMb
 :      .MMMMMMMMMMMMMMMMMMM/HMMMMM|  `9MM'HL
:       {MMMMMMMMMMMMMMMMMMMM)MM*''    `H[ `9|
|       `HMMMMMMMMMMMMMMMMMMMMb##|      `F. :?
H        `"*"'"`#MMMMMMMMMMMMMMM?         '  k
M.               MMMMMMMMMMMMM"'             H
MMH.             `HMMMMMMMMMM:               |
&MM|              `MMMMMMMMMM,               -
`MM|              dMMMMMMMMMM|.oH            :
 9ML              `HMMMMMMM?  dH'            -
  Hi               |MMMMMMP   "'            .'
   T.               `MMM#'                 -'
    `.               `                   .`
      `                                -'
        `.. .                       ..'
            ...                  .-'
              '-. //######M#b~""'
    """, 
    """
              _ooq=""''$b$_&?b)_
          .-`^"  "'o |&M:MMMMMMMMHo_
        o/'      -$Mb#MMMMMMMMMMMMMMHo.
      /'        .ooHP*&R&MMMMMMMMMMMMMM?.
    .'          `MRbod?|'`+?##9MMMMMMMMMH)
  .`          .,MMMMMMH#od##obdMMMMHMMMMMMb
  -          ?MMMMMMMMMMMMMMMMM$HMMH$ZP*HMMb
 ?          |MMMMMMMMMMMMMMMMMMM|9MMMMP  "M6)
.-          dMMMMMMMMMMMMMMMMMMMMb]M*'    |R |
1|          `HMMMMMMMMMMMMMMMMMMMMMd#|     ?,:
MH,          ``*""'"*#MMMMMMMMMMMMMM*       '`
MM6_                 |MMMMMMMMMMMMH"         :
MMMMMb.               "MMMMMMMMMMT           -
&MMMMM'                |MMMMMMMMMH           `
!MMMMb                .HMMMMMMMMM+.?&        :
 TMMMM                 *MMMMMMMP  dH' .     :
  9MM'                 `MMMMMMP'  "'       .'
   9ML                  `MMM#'            -'
    `H                   `               :
      `).                              .'
        `-)  .                      .-'
          ' ._                   .-`
              '-). ,b#####p&**^`'
    """



      
  ]


def main(stdscr):
  stdscr = curses.initscr()
  curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
  while True:

    for i in range(len(globe)):
      stdscr.clear()

      stdscr.addstr(0, 0, globe[i], curses.color_pair(1))
      stdscr.refresh()

      time.sleep(.1)

  stdscr.getch()
wrapper(main)

