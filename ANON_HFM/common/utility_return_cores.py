#script to generate the decisions and localization for Return_cores (return cores) decisions
#Return_coresdump.txt goes in decisions\Return_cores.txt
#Return_coresdump.csv goes in 00_ANON_Return_coresdump.csv
infile = open("countries.txt", "r")
outfile = open("Return_coresdump.txt","w")
outfile2 = open("Return_coresdump.csv","w")
for line in infile:
    if len(line) > 5:
        if line[5] == "=":
            tag = line[0:3]
            if tag != "REB":
                newline = "return_cores_" + tag + " = { picture = return_cores_img alert = no potential = { ai = no has_country_flag = return_cores_decision " + tag + " = { NOT = { substate_of = THIS } OR = { in_sphere = THIS vassal_of = THIS } } any_owned_province = { is_core = " + tag + " NOT = { is_core = THIS } } } allow = { war = no " + tag + " = { war = no } } effect = { prestige = -5 relation = { who = " + tag + " value = 50 } any_owned = { limit = { NOT = { is_core = THIS } is_core = " + tag + " } secede_province = " + tag + " } } } \n"
                outfile.write(newline)
                country = line.split("/")[1].split(".")[0]
                newline = "return_cores_" + tag + "_title;Return cores to "+ country +" ;;;;;;;;;;;;x,,\n"
                newline2 = "return_cores_" + tag + "_desc;We hold provinces that " + country + " has claims on. Returning these provinces, as an act of good faith, would surely bolster our relations.;;;;;;;;;;;;x\n"
                outfile2.write(newline)
                outfile2.write(newline2)

infile.close()
outfile.close()
outfile2.close()
