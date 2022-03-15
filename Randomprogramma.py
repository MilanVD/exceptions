while True:
    try:
        Gender = int(input('Bent u man of vrouw? : '))
    except ValueError:
        print('grapje dat boeit mij niet')
    else:
        print(f'u bent dus een...: {Gender}')
        break
    finally:
        print('het boeit me nogsteeds niet')
    