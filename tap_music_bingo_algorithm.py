import random
import os.path
import spotify_functions

playlist = spotify_functions.for_bingo

count = 0
for i in range(0,10): # Change second number in range to raise or lower the number of boards created
    count += 1
    temp_playlist = playlist[:]
    card_list = []
    for j in list(range(1,25)):
        rando = random.randint(1, len(temp_playlist)-1)
        card_list.append(temp_playlist[rando])
        temp_playlist.pop(rando)

    board_HTML = (
    '''
    <!DOCTYPE html>
    <html>
        <body>
            <table style="width: 50%"; class="center">
                <tr style= "height:50px">
                    <th><img src="https://fastly.4sqi.net/img/general/600x600/467684390_3w2clz01w7egoXWuZpwK5Ld7s9YSW_GIkd_yzCmC_h0.png" style="height:10%; width:10%"></th>
                    <th><h3>Music Bingo</h3></th>
                </tr>
            <table style="width: 50%"; class="center">
                <tr style = "height: 50px" bgcolor="green"> <!-- Header Row --->
                    <th>B</th>
                    <th>I</th>
                    <th>N</th>
                    <th>G</th>
                    <th>O</th>
                </tr>
                <tr style = "height: 50px"> <!-- Row 1 --->
                    <th>{song1}</th>
                    <th>{song2}</th>
                    <th>{song3}</th>
                    <th>{song4}</th>
                    <th>{song5}</th>
                </tr>
                <tr style = "height: 50px"> <!-- Row 2 --->
                    <th>{song6}</th>
                    <th>{song7}</th>
                    <th>{song8}</th>
                    <th>{song9}</th>
                    <th>{song10}</th>
                </tr>
                <tr style = "height: 50px"> <!-- Row 3 --->
                    <th>{song11}</th>
                    <th>{song12}</th>
                    <th>FREE</th>
                    <th>{song13}</th>
                    <th>{song14}</th>
                </tr>
                <tr style = "height: 50px"> <!-- Row 4 --->
                    <th>{song15}</th>
                    <th>{song16}</th>
                    <th>{song17}</th>
                    <th>{song18}</th>
                    <th>{song19}</th>
                </tr>
                <tr style = "height: 50px"> <!-- Row 5 --->
                    <th>{song20}</th>
                    <th>{song21}</th>
                    <th>{song22}</th>
                    <th>{song23}</th>
                    <th>{song24}</th>
                </tr>
            </table>
            <p>
            <br>
            <br>
            </p>
        </body>
    </html>''').format(
                    song1 = card_list[0],
                    song2 = card_list[1],
                    song3 = card_list[2],
                    song4 = card_list[3],
                    song5 = card_list[4],
                    song6 = card_list[5],
                    song7 = card_list[6],
                    song8 = card_list[7],
                    song9 = card_list[8],
                    song10 = card_list[9],
                    song11 = card_list[10],
                    song12 = card_list[11],
                    song13 = card_list[12],
                    song14 = card_list[13],
                    song15 = card_list[14],
                    song16 = card_list[15],
                    song17 = card_list[16],
                    song18 = card_list[17],
                    song19 = card_list[18],
                    song20 = card_list[19],
                    song21 = card_list[20],
                    song22 = card_list[21],
                    song23 = card_list[22],
                    song24 = card_list[23])

    save_path = "Tap_Putt/BINGO/Boards"
    file_id = 'Bingo_boards'
    file_name = os.path.join(save_path, file_id+'.html')

    if count == 0:
        file = open(file_name,"w") # create file
        file.write(board_HTML)
        file.close()
    else:
        file1 = open(file_name, "a")  # append to file
        file1.write(board_HTML)
        file1.close()