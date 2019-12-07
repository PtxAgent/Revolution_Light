csv_format = False

for rounds in range (0, 6, 1):
    a = []
    xp_field = 0
    val_field = 0
    xp_disc = 0
    val_disc = 0
    xp_spec = 0
    val_spec = 0

    val = 0
    val_per_spec = 0
    xp = 0

    val_attrib = 0

    if (rounds<3):
        num_disc = 1
        num_spec_disc_1 = rounds + 1
    else:
        num_disc = 2
        num_spec_disc_1 = 2

    if (rounds<3):
        num_spec_disc_2 = 0
    else:
        num_spec_disc_2 = rounds - 2

    for field in range(1, 11, 1):
        xp_field += field
        xp_disc = 0
        for Discipline in range(1, 11, 1):
            xp_disc += Discipline * 2 * num_disc
            xp_spec = 0
            for specialization in range(1, 11, 1):
                xp_spec += specialization * 3 * num_spec_disc_1 + specialization * 3 * num_spec_disc_2
                xp = xp_disc + xp_field + xp_spec
                val_per_spec = ( field + Discipline * 2 + specialization * 3 )
                val = val_per_spec * (num_spec_disc_1 + num_spec_disc_2)

                val_attrib = field + Discipline * 2 * num_disc +  specialization * 3 * (num_spec_disc_1 + num_spec_disc_2)

                a.append([field, Discipline, specialization, xp, val_per_spec, val, val/xp, val_attrib])
        b = sorted(a, key=lambda x:(x[5], x[3]),  reverse=False)

    if (num_disc == 1):
        print("\nOne Discipline in Field; Number of Specializations: %d" % num_spec_disc_1)
    else:
        print("\nTwo Disciplines in Field;")
        print("Number of Specializations in 1st tree: %d, number of Specializations in 2nd tree: %d \n" % (num_spec_disc_1, num_spec_disc_2))

#    print("\nNumber of Specializations in tree: %d/%d" % (num_spec_disc_1, num_spec_disc_2))
    # for i in b:
    #     print("Field: %d:  Discipline: %d, Specialization: %d  -->> XP spent: %d, value per Specialization: %d, "
    #           "value: %d, ratio: %f " % (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    if ( csv_format ):
        print("Field,Discipline,NumDisc,Specialization,NumSpecTree1,NumSpecTree2,XP spent,value per Spec, value, ratio, value attributes")

        for j in a:
            print("%2d,%2d,x%d,%2d,x%d,x%d,%4d,%2d,%3d,%f,%3d" % (j[0], j[1], num_disc, j[2], num_spec_disc_1,
                                                                num_spec_disc_2, j[3], j[4], j[5], j[6], j[7]))

    else:
        actval = 0
        for j in b:
            if (j[4] > actval):
                print("Field: %2d:  Discipline: %2d (x%d) Specialization: %2d (x%d/x%d)  -->> "
                      "XP spent: %4d, value per Specialization: %2d, "
                      "value: %3d, ratio: %f, value attribute points: %3d "
                      % (j[0], j[1], num_disc, j[2], num_spec_disc_1, num_spec_disc_2,
                                                 j[3], j[4], j[5], j[6], j[7]))
            actval = j[4]
