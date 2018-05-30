import numpy

def create_prefix(input_method):
    if input_method == 1:
        prefix = '''$molecule
0 1
'''
    elif input_method == 2:
        prefix = '''%nprocshared=24
%chk=noname.chk
%mem=80GB
# td=(singlets, nstates=6, root=2) b3lyp/cc-pvtz
conformation 1 - S1
0 1
'''
    return prefix

def create_suffix(input_method):
    if input_method == 1:
        suffix = '''
$end

$rem
jobtype opt
method soscis(d)
basis cc-pvdz
aux_basis rimp2-cc-pvdz
cis_n_roots 4
cis_singlets true
cis_triplets false
gui 2
mem_total 40000
mem_static 2000
cis_state_deriv 1
symmetry false
$end


'''
    elif input_method == 2:
        suffix = '''

'''

    return suffix



def create_fd_geoms(xyz, fd_step_size, input_method):
    
    del_x = fd_step_size

    prefix = create_prefix(input_method)
    
    suffix = create_suffix(input_method)

    for i in range(len(xyz)):
        f = open('x_'+str(i)+'_p.inp',"w+")
        f.write(prefix)
        f.write(xyz[0][0])
        f.write(suffix)
        f.close

