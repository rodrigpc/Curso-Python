def calcula(hora,qhora):

    salariob = hora * qhora
    fgts = (salariob * 11) / 100
    sind = 0
    alqt = 0
    if salariob <= 900:
        salariol = salariob - sind

    elif salariob > 900 and salariob <=  1500:
        ir = (salariob * 5) / 100
        salariol = salariob - ir - sind
        alqt = 5
    elif salariob > 1500 and salariob <= 2500:
        ir = (salariob * 10) / 100
        salariol = salariob - ir - sind
        alqt = 10
    else:
        ir = (salariob * 20) / 100
        salariol = salariob - ir -sind
        alqt = 20
    inss = salariol*0.1
    totdesc =  fgts+inss+ir
    salariol = salariob - totdesc
    print("Salário Bruto: (%3d" % hora," * %3d" % qhora,"): R$ %7.2f"   % salariob)
    print("(-) IR (%2d" % alqt,"%)               :","R$ %7.2f" % ir )
    print("(-) INSS (10","%)","            : R$ %7.2f" % inss )
    print("(-) FGTS (11","%)","            : R$ %7.2f" % fgts)
    print("Total de descontos          : R$ %7.2f" % totdesc)
    print("Salário Liquido             : R$ %7.2f" % salariol)
    print("***********************************************")
    print("Você informou que seu salário hora é de : R$ %7.2f" % hora)
    print("Você informou que a qtda de horas é de :  %7d" % qhora)


def main():
    hora = int(input("Informa o valor recebido por hora trabalhada. "))
    qhora = int(input("Informe a quantidade de horas trabalhadas no mes. "))
    calcula(hora,qhora)

if __name__ == '__main__':
    main()
