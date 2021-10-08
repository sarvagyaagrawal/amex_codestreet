import cvxpy as cp

def optimize_values(saving,spending,income,minimum):

  #please include minimum_amount as function parameter
    x1=cp.Variable(pos=True)
    x2=cp.Variable(pos=True)
    
    
    constraint1=[saving*x1>=0,
                saving*x1<=income,
                saving*x1>=spending,
                
                x1>=0
                    
    ]
    constraint2=[
                spending*x2+ +saving*x1<=income,
                x2>=0.5,
                # spending*x1>=minimum,
                x2<=1
    ]

    
    objective_fn1=x1
    objective_fn2=x2
    

    problem3 = cp.Problem(cp.Maximize(objective_fn1),constraint1)
    problem3.solve(verbose=True)

    problem4 = cp.Problem(cp.Minimize(objective_fn2),constraint2)
    problem4.solve(verbose=True,solver='SCS')
    assert problem3.is_dqcp()
    assert problem4.is_dqcp()
    
    
    return int((x1.value))*saving*6, int((x2.value))*spending*6
