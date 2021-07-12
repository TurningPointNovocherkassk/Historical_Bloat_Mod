#script to generate the decisions and localization for gtfo (release vassal) decisions
#gtfodump.txt goes in decisions\gtfo.txt
#gtfodump.csv goes in 00_ANON_gtfodump.csv
infile = open("countries.txt", "r")
outfile = open("gtfodump.txt","w")
outfile2 = open("gtfodump.csv","w")
for line in infile:
    if len(line) > 5:
        if line[5] == "=":
            tag = line[0:3]
            if tag != "REB":
                newline = "gtfo_" + tag + " = { picture = gtfo alert = no potential = { ai = no has_country_flag = gtfo " + tag + " = { vassal_of = THIS NOT = { substate_of = THIS } } } allow = { war = no " + tag + " = { war = no } } effect = { prestige_factor = -0.1 release_vassal = " + tag + " diplomatic_influence = { who = " + tag + " value = -100 } } }\n"
                outfile.write(newline)
                country = line.split("/")[1].split(".")[0]
                newline = "gtfo_" + tag + "_title;Grant "+ country +" Independence;;;;;;;;;;;;x,,\n"
                newline2 = "gtfo_" + tag + "_desc;We've had a good run, but it's time to end our rulership of " + country + ": if you love something, let it go!;;;;;;;;;;;;x\n"
                outfile2.write(newline)
                outfile2.write(newline2)

infile.close()
outfile.close()
outfile2.close()
